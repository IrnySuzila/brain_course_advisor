import streamlit as st
# Display image
st.image("CourseAdvisor Logo 3.PNG")

class BrainBasedCareerAdvisor:
    def __init__(self):
        self.questions = [
            "1) Do you prefer a) working with numbers or b) creating art?",
            "2) What are your favorite activities, a) like solving puzzles or b) drawing?",
            "3) Do you enjoy a) reading or b) watching movies?",
            "4) Do you like to a) follow instructions or b) create your own way of doing things?",
            "5) Do you enjoy a) logic games or b) creative storytelling?",
            "6) Do you prefer a) detailed tasks or b) big-picture ideas?",
            "7) Do you like to work in a) an organized environment or b) a more flexible one?",
            "8) Do you follow a) a schedule or b) do things spontaneously?",
            "9) Do you prefer a) structured learning or b) hands-on projects?",
            "10) Do you enjoy a) critical thinking or b) imaginative thinking more?"
        ]
        self.career_suggestions = {
            'left_brained': ['Engineer', 'Accountant', 'Data Analyst', 'Financial Analyst', 'Software Developer', 'Doctor', 'Lawyer', 'Architect', 'Economist', 'Programmer'],
            'right_brained': ['Multimedia Animator', 'Writer', 'Fashion Designer', 'Interior Designer', 'Musician', 'Photographer', 'Journalist', 'Dancer', 'Actor', 'Writer'],
            'balanced_brained': ['Educator/Teacher', 'Entrepreneur', 'IT Manager', 'UI/UX Designer', 'Marketing Manager', 'Business Analyst', 'Researcher', 'Data Scientist', 'Project Manager', 'Lecturer']
        }

        self.course_suggestions = {
            'Engineer': ['Mechanical Engineering', 'Electrical Engineering', 'Civil Engineering'],
            'Accountant': ['Accounting', 'Finance', 'Business Administration'],
            'Data Analyst': ['Computer Science', 'Information Technology', 'Data Science'],
            'Financial Analyst': ['Finance', 'Business Administration(Finance)', 'Economic(Finance)'],
            'Software Developer': ['Computer Science', 'Information Technology', 'Software Engineering'],
            'Doctor': ['Medicine and Surgery', 'Dental Surgery', 'Veterinary science'],
            'Lawyer': ['Laws', 'Law with Shariah Law'],
            'Architect': ['Architecture'],
            'Economist': ['Economics', 'Business with Commerce(majoring in Economics'],
            'Programmer': ['Software Engineering', 'Computer Science', 'Information Technology'],
            'Multimedia Animator': ['Animation', 'Multimedia', 'Graphic Design'],
            'Writer': ['Creative Writing', 'English Literature', 'Communication (majoring in Journalism and Professional Writing'],
            'Fashion Designer': ['Fashion Design', 'Fashion Merchandising and Management', 'Fashion Design and Technology'],
            'Interior Designer': ['Interior Design', 'Interior Architecture'],
            'Musician': ['Music', 'Fine Art -Performing Art (Music)'],
            'Photographer': ['Photography', 'Film and Video Production', 'Visual Art (Photography and Videography Concentration)'],
            'Journalist': ['Journalism', 'Mass Communication'],
            'Dancer': ['Art-Dance', 'Fine Art-Dance'],
            'Actor': ['Acting', 'Performing Arts', 'Theater/Drama'],
            'Educator/Teacher': ['Education', 'TESL', 'Early Childhood Education'],
            'Entrepreneur': ['Business Administration (Majoring in Entrepreneurship)', 'Commerce (Majoring in Entrepreneurship)', 'Business and Entrepreneurship'],
            'IT Manager': ['Information Technology', 'Computer Science', 'Software Engineer'],
            'UI/UX Designer': ['Design(Majoring in UI/UX Design)', 'Human  Computer Interaction', 'Graphic Design (Majoring in UI/UX Design)'],
            'Marketing Manager': ['Busines Administration (majoring in Marketing', 'Communication', 'Digital Marketing'],
            'Business Analyst': ['Business Administration (majoring in Business Analytics', 'Business Analytic/Data Science', 'Economics/Business Economics'],
            'Researcher': ['Research Studies', 'Science chosen field', 'Art chosen field'],
            'Data Scientist': ['Data Science', 'Computer Science (Majoring in Data Science/AI', 'Mathematics/Statistic'],
            'Project Manager': ['Business Administration (majoring in Project Management)', 'Business/Management (majoring in Project Management)', 'Project Management/Operation Management'],
            'Manager': ['Business Administration (majoring in Management)', 'Business Management/Operation Management', 'Business/Management'],
            'Lecturer': ['Degree and Master in Chosen Field', 'Doctorate in Chosen Field']
        }

    def determine_brain_dominance(self, answers):
        left_brain_count = sum(1 for answer in answers if answer == 'A')
        right_brain_count = sum(1 for answer in answers if answer == 'B')

        if left_brain_count > right_brain_count:
            return 'left_brained'
        elif right_brain_count > left_brain_count:
            return 'right_brained'
        else:
            return 'balanced_brained'

    def suggest_careers_and_courses(self, dominance):
        careers = self.career_suggestions[dominance]
        return careers

    def get_course(self, chosen_career):
        courses = self.course_suggestions.get(chosen_career, [])
        return courses

advisor = BrainBasedCareerAdvisor()

def main():
    st.markdown(f"<br>", unsafe_allow_html=True)
    st.write("<b>Welcome to the Brain-based Course Advisor Application. I will ask you 10 questions to determine your brain dominance and suggest suitable careers and courses for you.</b>", unsafe_allow_html=True)
    st.markdown(f"<br>", unsafe_allow_html=True)

    # Check if state variables are initialized
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    if 'dominance' not in st.session_state:
        st.session_state.dominance = None
    if 'careers' not in st.session_state:
        st.session_state.careers = []
    if 'chosen_careers' not in st.session_state:
        st.session_state.chosen_careers = []

    # Collect answers
    answers = []
    for i, question in enumerate(advisor.questions):
        st.markdown(f"<h6>{question}</h6>", unsafe_allow_html=True)
        answer = st.radio("", ('A', 'B'), key=f"q_{i}")
        answers.append(answer)
        st.markdown(f"<br>", unsafe_allow_html=True)

    # Store answers in session state
    st.session_state.answers = answers
    st.markdown(f"<br>", unsafe_allow_html=True)
    
    if st.button("Submit"):
        # Determine brain dominance and suggest careers
        st.session_state.dominance = advisor.determine_brain_dominance(st.session_state.answers)
        st.markdown(f"<br>", unsafe_allow_html=True)
        
        st.write(f"<b>Based on your answers, you are:</b> {st.session_state.dominance.replace('_', ' ')}.",unsafe_allow_html=True)
                
        st.session_state.careers = advisor.suggest_careers_and_courses(st.session_state.dominance)
                        
    if st.session_state.careers:
        # Allow multiple selections using st.multiselect
        st.markdown(f"<br>", unsafe_allow_html=True)
        st.write("<b>The following are some career options for you. Which career(s) are you most interested in?:</b>", unsafe_allow_html=True)
        st.session_state.chosen_careers = st.multiselect('', st.session_state.careers, key='career_choices')
        
        st.markdown(f"<br>", unsafe_allow_html=True)
                
    # Display courses for each chosen career
    if st.session_state.chosen_careers:
        for career in st.session_state.chosen_careers:
            courses = advisor.get_course(career)
            if courses:  # Check if there are courses for the career
                st.write(f"<b>To pursue this career, you can consider the courses in the following field/domain :</b>", unsafe_allow_html=True)
               
                for idx, course in enumerate(courses, 1):
                    st.write(f"{idx}. <b>{course}</b>", unsafe_allow_html=True)  
            else:
                st.write(f"<b>No course suggestions available for</b> {career}.",unsafe_allow_html=True)
                st.markdown(f"<br>", unsafe_allow_html=True)
    # Title and description of the web application
            st.write('<br><br><b>Left-brain dominance</b> is often associated with characteristics related to logical, analytical, and detail-oriented thinking.<br>', unsafe_allow_html=True)
            st.write('<b>Right-brain dominance</b> is generally associated with traits related to creativity, intuition, and holistic thinking.<br>', unsafe_allow_html=True)
            st.write('<b>Balanced-brain dominance</b> refers to a cognitive style where an individual effectively integrates both left-brain and right-brain characteristics. This balance allows for a versatile approach to thinking and problem-solving.<br>', unsafe_allow_html=True)
            st.write('<b>Besides the suggested career and course, you can explore other related careers and course that you think are suitable for your future based on your brain-hemisphere dominance characteristics.</b>', unsafe_allow_html=True)
            #st.markdown(f"<br>", unsafe_allow_html=True)
    # Disclaimer
            st.write('<br><br><b>Disclaimer</b>: The information and recommendations provided by this brain-based career and course advisor app are intended for general guidance and informational purposes only and should not be construed as professional career advice. While the app utilizes advanced algorithms and cognitive science principles to offer career insights, it does not guarantee specific outcomes or results. Users should consult with qualified career professionals or advisors before making any significant career decisions. The developers of this app expressly disclaim any liability for any actions taken or not taken based on the information provided, and users assume all risks associated with their use of the app.', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
