# ... (keeping all imports and functions from before)

def show():
    """Display the study page."""
    init_session_state()

    st.markdown("""
        <div style='background: linear-gradient(90deg, #10b981 0%, #059669 100%);
                    padding: 2rem; border-radius: 12px; margin-bottom: 2rem;'>
            <h1 style='color: white; margin: 0; font-size: 2.5rem;'>Your Studies Companion</h1>
            <p style='color: #f0f0f0; margin-top: 0.5rem; font-size: 1rem;'>
                Multi-Agent Study Assistant: Generate comprehensive study materials powered by AI
            </p>
        </div>
    """, unsafe_allow_html=True)

    # ... (keeping sections 1, 2, 3 as before)
    
    # In the Quizzes tab (tabs[3]):
    with tabs[3]:
        st.markdown("### Quizzes and Exercises")
        
        if st.session_state.quizzes:
            quiz_data = parse_quiz(st.session_state.quizzes)
            
            total_questions = len(quiz_data["questions"])
            max_score = 20
            points_per_question = max_score / total_questions if total_questions > 0 else 0
            
            col_score1, col_score2 = st.columns([3, 1])
            with col_score1:
                st.progress(st.session_state.quiz_score / max_score if max_score > 0 else 0)
            with col_score2:
                st.markdown(f"### {st.session_state.quiz_score}/{max_score}")
            
            st.markdown("---")
            
            for q_idx, question in enumerate(quiz_data["questions"]):
                q_num = question["number"]
                
                st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                                padding: 1.5rem; border-radius: 12px; border: 1px solid #334155;
                                margin-bottom: 1.5rem;'>
                        <h4 style='color: #10b981;'>Q{q_num}: {question['question']}</h4>
                    </div>
                """, unsafe_allow_html=True)
                
                question_key = f"q_{q_num}"
                current_answer = st.session_state.quiz_answers.get(question_key, None)
                
                for option_key, option_text in question["options"].items():
                    is_selected = current_answer == option_key
                    is_correct = option_key == question["correct"]
                    
                    # Determine styling: PINK for selection, GREEN/RED after submission
                    if st.session_state.quiz_submitted:
                        if is_selected:
                            if is_correct:
                                bg_color = "#10b981"  # Green
                                border_color = "#059669"
                            else:
                                bg_color = "#ef4444"  # Red
                                border_color = "#dc2626"
                        else:
                            bg_color = "#1e293b"
                            border_color = "#334155"
                    else:
                        if is_selected:
                            bg_color = "#ec4899"  # PINK for selection
                            border_color = "#db2777"
                        else:
                            bg_color = "#1e293b"
                            border_color = "#334155"
                    
                    col_opt_label, col_opt_button = st.columns([0.08, 0.92])
                    
                    with col_opt_label:
                        st.markdown(f"**{option_key})**")
                    
                    with col_opt_button:
                        if not st.session_state.quiz_submitted:
                            # Create custom styled button
                            button_style = f"""
                                background: {bg_color}; 
                                color: white; 
                                padding: 0.75rem 1rem;
                                border: 2px solid {border_color}; 
                                border-radius: 8px;
                                margin-bottom: 0.5rem;
                                font-weight: 500;
                            """
                            
                            if st.button(
                                option_text,
                                key=f"btn_{question_key}_{option_key}",
                                use_container_width=True
                            ):
                                st.session_state.quiz_answers[question_key] = option_key
                                st.rerun()
                        else:
                            # Display only after submission
                            st.markdown(f"""
                                <div style='background: {bg_color}; color: white; padding: 0.75rem 1rem;
                                            border: 2px solid {border_color}; border-radius: 8px;
                                            margin-bottom: 0.5rem;'>
                                    {option_text}
                                </div>
                            """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
