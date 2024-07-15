
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.metrics import dp

Builder.load_file('the.kv')
Window.size=(240,500)
Window.top = 50
#fonts/HelveticaNeueMedium.otf
#fonts/helvetica-neue-5/HelveticaNeueRoman.otf
#fonts/helvetica-neue-5/HelveticaNeueHeavy.otf
LabelBase.register(name= 'Pacifico', fn_regular= 'fonts/Pacifico.ttf')
LabelBase.register(name= 'Recursive', fn_regular= 'fonts/Recursive.ttf')
LabelBase.register(name= 'PTSerif-Regular', fn_regular= 'fonts/PTSerif-Regular.ttf')
LabelBase.register(name= 'Tinos-Regular', fn_regular= 'fonts/Tinos-Regular.ttf')
LabelBase.register(name= 'HelveticaNeueRoman', fn_regular= 'fonts/helvetica-neue-5/HelveticaNeueRoman.otf')

class WelcomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class PsychologyScreen(Screen):
    
    #score = 1
    
    question_text = StringProperty("")
    answer_a_text = StringProperty("")
    answer_b_text = StringProperty("")
    answer_c_text = StringProperty("")
    answer_d_text = StringProperty("")

    selected_answer = StringProperty("")  # Track user selection
    correct_answer = StringProperty("")   # Store correct answer

    def __init__(self, **kwargs):
        super(PsychologyScreen, self).__init__(**kwargs)
        self.questions = [  # Replace with your questions (answer key included as 'ca' property)
            
        
            #1--------------------------------
            {"question": "The first two weeks of pre-natal development, characterised by rapid cell division, increased complexity, and differentiation in the uterine wall is called?   ",
            "answers": {"a": "embryo stage  ", "b": "foetal stage ", "c": "germinal stage ", "d": "gestation stage"},
            "ca": "c"
            },

            #2--------------------------------
            {"question": "‘Out of sight is out of mind’ is a good summary of the assertion that a child who has not mastered...  ",
            "answers": {"a": "conservation ", "b": "animism ", "c": "symbolic thought ", "d": "object permanence"},
            "ca": "d"
            },

            #3--------------------------------
            {"question": "The type of development from the central part of the body toward the outer direction is called?  ",
            "answers": {"a": "Cephalocaudal ", "b": "Cell maturation ", "c": "Maturation ", "d": "Proximodistal"},
            "ca": "d"
            },

            #4--------------------------------
            {"question": "During the pre-natal stage, which structure supplies maternal antibodies that provide the unborn child immunity against a number of infectious diseases?  ",
            "answers": {"a": "placenta ", "b": "yolk sac ", "c": "amniotic fluid ", "d": "amniotic sac"},
            "ca": "a"
            },

            #5--------------------------------
            {"question": "Araba is a pupil in Nipahiamoah primary school. Her teacher asked her to add 8 and 7. In an attempt to find an answer to the problem, Araba counted her fingers and toes. At what stage of cognitive development is Araba?   ",
            "answers": {"a": " Sensorimotor stage   ", "b": "Pre-operational stage ", "c": "Concrete operational stage  ", "d": "Formal operational stage"},
            "ca": "c"
            },
            
            #6--------------------------------
            {"question": "Which of the following is a domain of growth and development?  ",
            "answers": {"a": "Interactionalisation ", "b": "Intellectualisation ", "c": "Riding of a bicycle ", "d": "All options"},
            "ca": "d"
            },
            
            #7--------------------------------
            {"question": "Asani was able to give a vivid account of what happened last semester when students went on rampage. Which goal of psychology explains Asani's ability? ",
            "answers": {"a": "Description ", "b": "Modification ", "c": "Prediction ", "d": "Explanation"},
            "ca": "a"
            },

            #8--------------------------------
            {"question": "What are the two components of adaptation in Piaget's theory?",
            "answers": {"a": "Assimilation and adjustment ", "b": "Accommodation and adjustment ", "c": "Assimilation and Accommodation ", "d": "Adaptation and assimilation"},
            "ca": "c"
            },

            #9--------------------------------
            {"question": "Vygotsky's theory suggests that cognitive development is strongly influenced by....",
            "answers": {"a": "inherited traits and genetic factors ", "b": "individual cognitive abilities and intelligence", "c": "formal education and academic instruction ", "d": " social interactions and collaborative learning"},
            "ca": "d"
            },
            
            #10--------------------------------
            {"question": "Which of the following is true about physical and cognitive development in childhood and adolescence?",
            "answers": {"a": "They occur independently of each other", "b": "They have no impact on each other", "c": "They are completely determined by genetics", "d": "They interact and influence each other"},
            "ca": "d"
            },

            #11--------------------------------
            {"question": "You are watching a newborn when it is startled by a loud noise. The baby extends its arms and legs, then quickly brings them in as if trying to grasp something. This illustrates the....",
            "answers": {"a": "grasp reflex", "b": "tonic reflex", "c": " moro reflex", "d": "stepping reflex"},
            "ca": "c"
            },
            
            #12--------------------------------
            {"question": "When psychologists try to find out how people transform physically, intellectually, emotionally, and socially they focus on......",
            "answers": {"a": "learning", "b": "transition", "c": " maturation", "d": "growth and development process"},
            "ca": "d"
            },

            #13--------------------------------
            {
            "question": "The qualitative increase in the body of organism is termed as......",
            "answers": {"a": "adulthood", "b": "childhood", "c": "growth", "d": "development"},
            "ca": "d"},

            #14--------------------------------
            {
            "question": "A three-year-old child may run to a corper, turn his back to you, not realising that he is still in plain view. Based on Piaget's view, this is tan important feature of the...",
            "answers": {"a": "sensorimotor stage", "b": "pre-operational stage", "c": "concrete operational stage", "d": "formal operational stage"},
            "ca": "b"},
            
            #15--------------------------------
            {
            "question": "If an infant develops teeth, which were not there before, it is considered in psychology as....",
            "answers": {"a": "development", "b": "growth", "c": "Maturation", "d": "Transition"},
            "ca": "b"},

            #16--------------------------------
            {
            "question": "The stage of intellectual development and learning that lies just ahead the learner's current stage is called....",
            "answers": {"a": "mentoring", "b": "scaffolding", "c": "zone of proximal development", "d": "cognitive development"},
            "ca": "c"},

            #17--------------------------------
            {
            "question": "Adaptation in cognitive development as proposed by Piaget entails...",
            "answers": {"a": " assimilation and adjustment", "b": "adjustment and accommodation", "c": "assimilation and accommodation", "d": "equilibration and adjustment"},
            "ca": "c"},

            #18--------------------------------
            {
            "question": "Which of the following serves as a defence mechanism to the unborn baby?",
            "answers": {"a": "Amniotic Sac", "b": "Embryo", "c": "Placenta", "d": "Trophoblast"},
            "ca": "a"},

            #19--------------------------------
            {
            "question": "Which of the following is the correct order of the three periods of pre-natal development?",
            "answers": {"a": "Embryo, Ovum, Fetus", "b": "Geminal, Embryo, Fetus", "c": "Ovum, Fetus, Embryo", "d": "Fetus, Embryo, Ovum"},
            "ca": "b"},

            #20--------------------------------
            {
            "question": "Nyamekye's child is a day old, yet she is able to suck the mother's breast without being taught. What might be the reason to this ability of the child according to Piaget?", 
            "answers": {"a": "she has assimilation", "b": "she has adaptation", "c": "she has accommodation", "d": "she has schema"},
            "ca": "a"}, 
            
            #21------------
            {"question": "In a fertilized egg, the cell divides and expand outward to become an embryo. This is the principle of  ",
            "answers": {"a": "Development being sequential", "b": "Development being continuous ", "c": "Cephalocaudal principle ", "d": "Proximodistal principle"},
            "ca": "d"
            },
            #22----------
            {"question": "Piaget reasoned that before the individual can organize and interpret experiences, they must first…………? ",
            "answers": {"a": "Receive appropriate tuition ", "b": "Create schemas ", "c": "Intellectualize it ", "d": "Represent it mentally"},
            "ca": "b"
            },


            #23-----------
            {"question": "During prenatal period, the spinal cord develops and then the head, chest and trunk grow followed by the arms and legs. This is an example of ……",
            "answers": {"a": "Development is continuous ", "b": "Proximodistal principle ", "c": "Development is sequential ", "d": "Cephalocaudal principle"},
            "ca": "b"
            },
            #24---------------
            {"question": "According to research, structural abnormalities include deletions, translocation, inversions and duplication. Inversion is the process whereby ………….  ",
            "answers": {"a": "A portion of one chromosome is missing ", "b": "A portion of one chromosome is transferred to another chromosome and turned ", "c": "A portion of a chromosome is broken off and turned upside down and reattached", "d": "A portion of the chromosome is duplicated resulting in extra genetic material"},
            "ca": "c"
            },
            #25-------------
            {"question": "Which developmental theory was based on how each stage, a person experiences a crisis which could have a positive or negative outcome for personality development?  ",
            "answers": {"a": "Operant conditioning ", "b": "Psychosocial theory ", "c": "Cognitive theory", "d": "Classical"},
            "ca": "b"
            },
            #26--------------
            {"question": "A newborn will need support with the head, by two months after which the physical control will move downwards to the arms and to the legs. This phenomenon is termed as …………",
            "answers": {"a": "Cephalocaudal Principle ", "b": "Development is Sequential ", "c": "Proximodistal Principle", "d": "Development is Continuous"},
            "ca": "a"
            },
            #27-------------			
            {"question": "What characteristics are normally seen in the play patterns of the 4-year-old child?  ",
            "answers": {"a": "The 4-year-old puts toys away without supervision ", "b": "The 4-year-old frequently has imaginary playmates ", "c": "The 4-year-old enjoys a group of 5 or 6 peers", "d": "The 4-year-old engages in solitary and parallel play most of the time"},
            "ca": "b"
            },
            #28---------------
            {"question": "Environmental factors that shape development include all the following except……  ",
            "answers": {"a": "Quality of nutrition ", "b": "Intelligence ", "c": "Culture", "d": "Quality of learning"},
            "ca": "b"
            },
            #29-----------
            {"question": "Kofi is a teacher in Unipra JHS, he had an in-service training on threats to prenatal development. After the training, Kofi’s perceptions of his students changed. He is likely to do the following except, …………  ",
            "answers": {"a": "Refer students with medical conditions to the school nurse ", "b": "Design his instruction to suit all the students ", "c": "Collaborate with parents of students with special needs", "d": "Cane students who score low marks in class test"},
            "ca": "d"
            },
            #30------------
            {"question": "Trisomy 21 is caused by an extra copy of the 21st chromosome. It also known as ……  ",
            "answers": {"a": "Turner’s syndrome ", "b": "Klinefelter syndrome ", "c": "Down syndrome", "d": "Fragile X syndrome"},
            "ca": "c"
            },
            #31------------
            {"question": "Erikson’s stage of psychosocial development in which a child gains independence from caregivers is:  ",
            "answers": {"a": "Initiative vs guilt ", "b": "Autonomy vs shame and doubt ", "c": "Basic trust vs mistrust", "d": "Industry vs inferiority"},
            "ca": "b"
            },
            #32-----------
            {"question": "When becoming old and looking back, people tend to evaluate their life and want to know if they lived a successful life. At what stage of Erickson’s psychosocial stages is the above description synonymous to?  ",
            "answers": {"a": "Integrity vs despair  ", "b": "Identity vs role confusion ", "c": "Intimacy vs isolation", "d": "Generativity vs stagnation"},
            "ca": "a"
            },
            #33--------------
            {"question": "	Ama was born in 1985 and after 15 years Ama has increased in height, body parts have been magnified and also the organs and body systems. One could realize that Ama’s height, size and gait has changed. This phenomenon is termed ………...  ",
            "answers": {"a": "Changes ", "b": "Growth ", "c": "Maturity", "d": "Learning"},
            "ca": "b"
            },
            #34--------------
            {"question": "As Ekow became older, his brain developed in a way that meant he was able to handle more complex tasks than he could before. This phenomenon meant that Ekow is/has………… ",
            "answers": {"a": "Changed ", "b": "Grown ", "c": "Matured", "d": "Learned"},
            "ca": "c"
            },
            #35----------
            {"question": "As a child develops, he or she adds to the skills already acquired and the new skills become the basis for further achievement and mastery of skills. This is an instance of   ",
            "answers": {"a": "Development being Sequential ", "b": "Proximodestal Principle ", "c": "Cephalocaudal Principle", "d": "Development being Continuous"},
            "ca": "d"
            },

            #36---------------
            {"question": "	Growth is Asynchronous. This means…………... ",
            "answers": {"a": "There are individual rates of growth ", "b": "Growth proceeds from center upwards ", "c": "Growth is characterized by critical periods", "d": "It is influenced by environmental factors"},
            "ca": "a"
            },
            #37-----------
            {"question": "A baby boy with klinefelter syndrome is known to have…………… ",
            "answers": {"a": "Ocular Albinism (OAI) on the X chromosome ", "b": "An extra X chromosome in most of its cell ", "c": "A breakage of the tip of an X chromosome", "d": "An extra Y chromosome"},
            "ca": "b"
            },
            #38------------
            {"question": "	Kwame and Ama are planning to get married and have children. Kwame is a carrier of the sickle cell disease. Ama has a normal hemoglobin gene combination. What is their percentage chance of having children who do NOT have the sickle trait? ",
            "answers": {"a": "50% ", "b": "100% ", "c": "25%", "d": "0%"},
            "ca": "a"
            },
            #39----------
            {"question": "Piaget’s theory of cognitive development began with his study of: ………. ",
            "answers": {"a": "Mollusks ", "b": "Children ", "c": "sRhesus monkeys", "d": "Dogs"},
            "ca": "b"
            },
            #40---------
            
            {"question": "Pick the odd one out……… ",
            "answers": {"a": "Zygote ", "b": "Fetus ", "c": "Embryo", "d": "Ovum"},
            "ca": "d"
            },

            #41------------------
            {"question": "The following influences growth except, …………….",
            "answers": {"a": "Genetics ", "b": "Disease ", "c": "Nutrition", "d": "Social status"},
            "ca": "d"
            },
            
            #42-------------
            {"question": "Physical characteristics such as weight, height, skin, color and psychological characteristics such as intelligence and personality are synonymous to? …………",
            "answers": {"a": "Phenotype ", "b": "Zygote ", "c": "Genotype", "d": "Chromosome"},
            "ca": "a"
            },
            #43------------
            {"question": "	The cognitive stage in which abstract thought emerges is: …………...",
            "answers": {"a": "Concrete operational stage ", "b": "Preoperational stage ", "c": "Sensorimotor stage", "d": "Formal operational stage"},
            "ca": "d"
            },
            #44------------
            {"question": "Hemophilia A&B is more prevalent in female children …………",
            "answers": {"a": "True ", "b": "False ", "c": "Both", "d": "None of the above"},
            "ca": "b"
            },
            #45----------
            {"question": "All the following are periods of prenatal development except ………….",
            "answers": {"a": "Embryonic ", "b": "Germinal ", "c": "Postpartum", "d": "Fetal"},
            "ca": "c"
            },
            #46----------------
            {"question": "The cognitive abilities of an adolescent differ from that of a child primarily in that, unlike a child, an adolescent thinking is not necessarily tied to …………….",
            "answers": {"a": "Fantasy ", "b": "Concrete events ", "c": "Abstract ideas", "d": "Logic"},
            "ca": "b"
            },
            #47-------------
            {"question": "According to Erickson, which group of people are significant in integrity versus despair? ………….",
            "answers": {"a": "Household, workmates ", "b": "Friends, partners ", "c": "Peers, role models", "d": "Mankind, my kind"},
            "ca": "a"
            },

            #48-------------
            {"question": "In a Piagetian classroom, children are encouraged to discover themselves through spontaneous interaction with the environment, rather than the presentation of ready-made knowledge. ………….",
            "answers": {"a": "True ", "b": "False ", "c": "Both", "d": "None of the above"},
            "ca": "a"
            },
            #49------------
            {"question": "Piaget believed that extensive interaction with …………... is essential for each person’s cognitive development.",
            "answers": {"a": "Authority figures ", "b": "One’s own family ", "c": "Other children", "d": "The environment"},
            "ca": "d"
            },
            #50----------
            {"question": "I can be measured, and I am influenced by genetics. I am also characterized by quantity. Who am I?",
            "answers": {"a": "Growth ", "b": "Fetus ", "c": "Learning", "d": "Development"},
            "ca": "a"
            },
            #51---------
            {"question": "Kukua is married and found that she has the sickle cell trait and the husband too has sickle cell trait. What is their percentage chance of giving birth to a child who is sickle cell anaemic? ……………",
            "answers": {"a": "25 percent ", "b": "75 percent ", "c": "50 percent", "d": "100 percent"},
            "ca": "a"
            },
            #52-----------
            {"question": "At the germinal stage the sperm cell and the ovum (egg) combines to form a single cell called ………………",
            "answers": {"a": "Fetus ", "b": "Zygote ", "c": "Embryo", "d": "Ectoderm"},
            "ca": "b"
            },
            #53--------------
            {"question": "	According to Erickson, what virtue is exhibited in integrity versus despair? ………",
            "answers": {"a": "Love ", "b": "Care ", "c": "Wisdom", "d": "Competence"},
            "ca": "c"
            },
            #54-------------
            {"question": "Piaget theory of cognitive development is essentially about ……………...",
            "answers": {"a": "The influence of the social world on the growing child ", "b": "The development of the ability to think ", "c": "Therapeutic procedures to correct cognition", "d": "Problems in sensory-motor development"},
            "ca": "b"
            },	
            #55------------
            {"question": "Abena, beginning this week, has begun to engage in goal directed behavior, thus cause and effect relationship. Abena can be said to have developed………….",
            "answers": {"a": "Primary circular reaction ", "b": "Secondary circular reaction ", "c": "Tertiary circular reaction", "d": "Coordination of secondary circular reaction"},
            "ca": "c"
            },
            #56---------
            {"question": "The principle of human development which explains that a child’s first step occurs as a result of aggregation experience is……………….",
            "answers": {"a": "Proximodistal ", "b": "Cephalocaudal ", "c": "Epigenetic", "d": "Asynchronous"},
            "ca": "b"
            },

            #57------------
            {"question": "Adoma knows that quantity of objects remains same if nothing is added despite changes in spatial arrangement. Adoma has acquired the principle of ",
            "answers": {"a": "Object permanence ", "b": "Class inclusion ", "c": "Reversibility", "d": "Conservation"},
            "ca": "d"
            },
            #58----------
            {"question": "Before the nineteenth century, man tried to study himself via all the following EXCEPT",
            "answers": {"a": "Guesses ", "b": "Intuitions ", "c": "Superstitions", "d": "Speculations"},
            "ca": "b"
            },
            #59---------
            {"question": "Kobby was six inches tall two months ago, however as at yesterday he measured eight inches. Kobby has experienced……………….",
            "answers": {"a": "Improvement ", "b": "Maturation ", "c": "Growth", "d": "Development"},
            "ca": "c"
            },
            #60------------
            {"question": "Kwame my first son, before the lockdown could only brush his teeth. However, two weeks in the lockdown, Kwame can bath as well. Kwame is said to have……………...",
            "answers": {"a": "Matured ", "b": "Developed ", "c": "Grown", "d": "Learned"},
            "ca": "d"
            },
            #61------------
            {"question": "In experimental research, the group that receives the treatment is called the………..group.",
            "answers": {"a": "Confounded ", "b": "Controlled ", "c": "Experimental", "d": "Extraneous"},
            "ca": "c"
            },
            #62-----------
            {"question": "Akosua sees herself as the most intelligent and pretty girl in the whole Mampong municipality. What concept explains Akosua’s behavior?",
            "answers": {"a": "Selfishness ", "b": "Egocentrism ", "c": "Animillism", "d": "Conservation"},
            "ca": "b"
            },
            #63-----------
            {"question": "If two variables are directly correlated, a change in one variable is accompanied by a ………… change in the other. ",
            "answers": {"a": "Exponential ", "b": "Positive ", "c": "Negative", "d": "Progressive"},
            "ca": "b"
            },
            #64-----------
            {"question": "Adwubi initially could not do simple multiplication, however, after receiving tutorial from her sister on the use of the multiplication table, she has overcome her initial difficulty. Adwubi achieved this milestone as result of……………...",
            "answers": {"a": "Zone of proximal development ", "b": "Trial and error ", "c": "Imitation", "d": "Scaffolding"},
            "ca": "d"
            },
            #65-----------
            {"question": "Adwoa was told by a midwife to be aware of continuum of biological and environmental conditions that are used to identify children whose well-being are at risk. This advice Adwoa received highlights…………….",
            "answers": {"a": "Developmental risk ", "b": "Teratogens ", "c": "Embryopathy", "d": "Genetic disorders"},
            "ca": "b"
            },
            #66-----------
            {"question": "My aim is to assist people to understand how human language has evolved over the thousands of year of human existence. My proper name should be …",
            "answers": {"a": "Clinical psychology ", "b": "Language psychology ", "c": "Existence psychology", "d": "Educational psychology"},
            "ca": "b"
            },
            #67-----------
            {"question": "Once Kwesi was born there was that expectation that he will have the full complement of all his 32 teeth as the years go by, even though at 2 months his mouth looked hollow. This means that: ",
            "answers": {"a": "Growth is asynchronous ", "b": "Growth is unpredictable ", "c": "Growth is sequential", "d": "Growth is predictable"},
            "ca": "d"
            },
            #68-----------
            {"question": "Which of the following cannot be included in the paternal causes of prenatal abnormalities?",
            "answers": {"a": "Inducing of maternal stress by father of unborn baby ", "b": "Poor working environment of father of unborn baby", "c": "Strenuous exercising by father of unborn baby", "d": "Illicit use of drugs of father of unborn baby"},
            "ca": "b"
            },
            #69-----------
            {"question": "When Baby Adwoa is startled by sudden noise, she throws both her two hands and legs up and begins crying. This is an example of a:",
            "answers": {"a": "Babinski Reflex ", "b": "Startled Reflex ", "c": "Uncomfortable Reflex", "d": "Moro Reflex"},
            "ca": "d"
            },
            #70-----------
            {"question": "They were born at the same time. How can one be more intelligent than the other”? Mrs. Addico grumbled. What process is Mrs. Addico misunderstanding?  ",
            "answers": {"a": "Growth ", "b": "Intelligence ", "c": "Maturation", "d": "Development"},
            "ca": "d"
            },
            #71-----------
            {"question": "During Kofi’s first day at school, the parents informed you the teacher to take very good care of him, because he easily gets tired, bleeds profusely when cut, and has pains in the joints when the weather is cold. Kofi must be suffering from………….?",
            "answers": {"a": "Rubella disease ", "b": "Ocular Albinism ", "c": "Sickle cell disease", "d": "Childhood jaundice"},
            "ca": "c"
            },
            #72-----------
            {"question": "	Mummy! Mummy!! Look I have hairs in my armpit and my voice has change, am now a man. Robert told the mother. Which field of psychology explains these changes",
            "answers": {"a": "Anatomy psychology ", "b": "Developmental psychology ", "c": "Abnormal psychology", "d": "Social psychology"},
            "ca": "b"
            },
            #73-----------
            {"question": "Two-year-old David’s ability to move and manipulate objects is an example of……...?",
            "answers": {"a": "Reflexive reactions ", "b": "Muscle coordination ", "c": "Developmental milestone", "d": "Motor skills"},
            "ca": "d"
            },
            #74------------
            {"question": "I normally work with judges to ensure that the truth prevails and that no innocent person is convicted to prison and no guilty person is acquitted because of an error in the evidence. who am I? ",
            "answers": {"a": "Prison psychology ", "b": "Forensic psychology ", "c": "Neuropsychology", "d": "Criminal psychology"},
            "ca": "b"
            },
            #75-----------
            {"question": "The socioemotional processes associated with human development has all the following components except:",
            "answers": {"a": "Changes in the individual’s personality ", "b": "Changes in the individual’s emotion ", "c": "Changes in the individual’s language", "d": "Changes in the individual’s relationship with others"},
            "ca": "c"
            },
            #76-----------
            {"question": "All reflexes in humans cease after infancy.",
            "answers": {"a": "True ", "b": "False ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },
            #77-----------
            {"question": "Bothe Agnes and Michael are six years old and in class 1. During Physical Education period, teacher Kuuku scolded Michael for not being able to pick up a small sack though Agnes could do so. What principle of growth and development is the teacher ignoring?",
            "answers": {"a": "Growth and development is continuous for individuals ", "b": "Growth and development is gradual for individuals ", "c": "Growth and development is epigenetic for individuals", "d": "Growth and development is different for individuals"},
            "ca": "d"
            },
            #78-----------
            {"question": "Having been born to very big parents Baby Jacob was bigger than all his contemporaries at 2 years. Baby Jacob’s situation is an example of the fact that………….?",
            "answers": {"a": "Development proceeds from general to specific ", "b": "Growth is genetic ", "c": "Growth is both quantitative and qualitative", "d": "Development is predictable"},
            "ca": "b"
            },
            #79-----------
            {"question": "In teaching, it is advised that teachers teach by starting from simple concepts to enable the students grasp the information before moving to more complex task. This is an example of …………………...",
            "answers": {"a": "Cephalocaudal principle ", "b": "Orthogenetic principle ", "c": "Continuous principle", "d": "Proximodistal principle"},
            "ca": "b"
            },
            #80-----------
            {"question": "	Clinical Psychology and counselling Psychology can be said to bedfellows.",
            "answers": {"a": "False ", "b": "True ", "c": "Both", "d": "All of the above"},
            "ca": "a"
            },
            #81-----------
            {"question": "Maturation is a subset of development",
            "answers": {"a": "False ", "b": "True ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },
            #82-----------
            {"question": "Development is more perceptible than growth.",
            "answers": {"a": "False ", "b": "True ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },
            #83-----------
            {"question": "	I regret coming to school, am not just happy because my grades are very bad. Which field of psychology will help this student to deal with her problem?",
            "answers": {"a": "Environmental psychology ", "b": "Developmental psychology ", "c": "Counselling psychology", "d": "Cognitive psychology"},
            "ca": "c"
            },
            #84-----------
            {"question": "At three years Thomas could not pick up 10kg bag of rice. However, when he turned 12 yrs. he picked it effortlessly. This relates to ………… than anything.",
            "answers": {"a": "Growth ", "b": "Maturation ", "c": "Strength", "d": "Development"},
            "ca": "a"
            },

            #85-----------
            {"question": "The subject matter of this branch covers psychological ways and means of improving all aspects of teaching or learning process, including the learner, learning process, learning material, learning environment and the teacher.",
            "answers": {"a": "Legal psychology ", "b": "Learning psychology ", "c": "Clinical psychology", "d": "Educational psychology"},
            "ca": "d"
            },

            #86-----------
            {"question": "Prenatal abnormalities in babies are mainly caused by genetic factors that are outside the control of the pregnant mother.",
            "answers": {"a": "True ", "b": "False ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },

            #87-----------
            {"question": "At the pre-conventional level of Kohlberg’s stages of moral development, the individual makes decisions based on consequences of their behavior.",
            "answers": {"a": "False ", "b": "True ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },

            #88-----------
            {"question": "	At the initiative versus guilt stage of Erikson, the individual normally feel rejected when he is not affirmative for trying something new.",
            "answers": {"a": "False ", "b": "True ", "c": "Both", "d": "All of the above"},
            "ca": "b"
            },

            #89-----------
            {"question": "Which of the following best describes infant reflexes in humans?",
            "answers": {"a": "Matured responses to stimuli before knowing what the stimuli is ", "b": "Innate behavioral responses to stimuli before knowing what the stimuli is ", "c": "Adaptive responses to stimuli before knowing what the stimuli is", "d": "Frightened responses to stimuli before knowing what the stimuli is"},
            "ca": "b"
            },

            #90-----------
            {"question": "Kofi Nimoh, a Nursery 1 4-year-old pupil, is not able to draw a circle very well. What principle of growth explains this situation?",
            "answers": {"a": "Growth is a continuous process ", "b": "Growth involves general movement to more specific movement ", "c": "Growth proceeds from the center of the body outwards", "d": "Growth is asymmetrical "},
            "ca": "d"
            },

            #91-----------
            {"question": "'After 30 years of working I don’t find any joy in working. At 60 years, I have nothing to prove. I want to focus on my children now'. What stage would Erikson consider this to be?",
            "answers": {"a": "Identity vs Role confusion ", "b": "Trust vs Mistrust ", "c": "Integrity vs Despair", "d": "Generativity vs Stagnation"},
            "ca": "d"
            },

            #92-----------
            {"question": "	'I deal with how humans are able to learn, communicate, perceive people and their environment, how to remember what they learn and solve problems'. Who am I?",
            "answers": {"a": "Para psychology ", "b": "Clinical psychology ", "c": "Cognitive psychology", "d": "Environment psychology"},
            "ca": "c"
            },


            #93-----------
            {"question": "	When growing Mensah was able to lift his hand firs before being able to hold a spoon in his hand. This is an example of…... ",
            "answers": {"a": "Growth and development is direction", "b": "Growth and development is sequential", "c": "Proximodistal development", "d": "Growth and development is gradual"},
            "ca": "d"
            },
            #94-----------
            {"question": "'I can’t disappoint my friends! They expect me to come to the party, Mummy. I don’t want them to feel I am abandoning them. I will do the chores when I come back. The party is important to me', Jessica told her mum and rushed out. Jessica’s morality is at:",
            "answers": {"a": "Universal Ethics Orientation", "b": "Obedience or Punishment", "c": "Self Interest Orientation Stage", "d": "Social Conformity Orientation"},
            "ca": "d"
            },
            #95-----------
            {"question": "Kwame knows the acceptable pattern of behavior but because of his hostile attitude, he willingly violates group expectations. Kwame is said to be having a/an………... act ",
            "answers": {"a": "Unsocial", "b": "Para social", "c": "Anti-social", "d": "Uni-social"},
            "ca": "c"
            }, 
            #96-----------
            {"question": "	Which of the following is true concerning prenatal exposure to smoke? ………",
            "answers": {"a": "Significantly increased infant growth ", "b": "Increased birth weight ", "c": "Increase risk of sudden infant death syndrome", "d": "Increased future behavioral performance"},
            "ca": "c"
            },
                        

        # Add more questions here
            
            
            
        ]
        self.current_question_index = 0
        self.question_number = 1
        self.load_question()

    def load_question(self):
        if self.current_question_index >= len(self.questions):
            # Handle end of quiz (switch screens, etc.)
            return
        current_question = self.questions[self.current_question_index]
        self.question_text = current_question["question"]
        self.answer_a_text = current_question["answers"]["a"]
        self.answer_b_text = current_question["answers"]["b"]
        self.answer_c_text = current_question["answers"]["c"]
        self.answer_d_text = current_question["answers"]["d"]
        self.correct_answer = current_question["ca"]
        self.selected_answer = ""  # Reset selection on new question

    def check_answer(self, answer):
        self.selected_answer = answer
        # Change button color based on selection (green for correct, red for incorrect)
        if answer == self.correct_answer:
            self.ids[answer + "_btn"].background_color = (0, 1, 0, 1)  # Green
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (1, 1, 1, 1)
            self.ids[answer + "_btn"].theme_text_color = 'Custom'
        else:
            self.ids[answer + "_btn"].background_color = (1, 0, 0, 1)  # Red
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (1, 1, 1, 1)
            self.ids[answer + "_btn"].theme_text_color = 'Custom'
            #self.ids.a_btn.canvas.before.children[0].radius = [40]

    def next_question(self):
        
        if self.question_number < 96:
            self.current_question_index += 1
            self.question_number += 1 
            self.ids.question_number.text = f"{self.question_number}"
        elif self.question_number == 96:
            self.current_question_index += 0
            self.question_number = 96 
            self.ids.question_number.text = f"{self.question_number}"
        self.load_question()
        # Reset button colors to default for next question
        for answer in ("a", "b", "c", "d"):
            self.ids[answer + "_btn"].background_color = (.9,.9,1,.5)  # White
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (0, 0, 0, 1)
            
    def previous_question(self):
        
        if self.question_number == 1:
            self.current_question_index -= 0
            self.question_number -= 0             
            self.ids.question_number.text = f"{self.question_number}"
            
            MDDialog( text = 'You can not go back!'
                
            )
        
        elif  self.question_number > 1:
            self.current_question_index -= 1
            self.question_number -= 1 
            self.ids.question_number.text = f"{self.question_number}"
        self.load_question()
        
        
        # Reset button colors to default for next question
        for answer in ("a", "b", "c", "d"):
            self.ids[answer + "_btn"].background_color = (.9,.9,1,.5)  # White
            self.ids[answer + "_btn"].color = (0, 0, 0, 1)

class ResultScreen(Screen):
    pass

class TrendsScreen(Screen):
    question_text = StringProperty("")
    answer_a_text = StringProperty("")
    answer_b_text = StringProperty("")
    answer_c_text = StringProperty("")
    answer_d_text = StringProperty("")

    selected_answer = StringProperty("")  # Track user selection
    correct_answer = StringProperty("")   # Store correct answer

    def __init__(self, **kwargs):
        super(TrendsScreen, self).__init__(**kwargs)
        self.questions = [  # Replace with your questions (answer key included as 'ca' property)
            
        
            #1-----------------------------
            {"question": "Which one of the following scholars defined leadership as an influence relationship among leaders and followers who intended real changes that reflect their mutual purposes?",
            "answers": {"a": "Rost  ", "b": "More ", "c": "Gardener", "d": "Northouse"},
            "ca": "a"
            },

            #2-----------------------------
            {"question": "All are common features of leadership except one.",
            "answers": {"a": "It involves a process", "b": "It involves high remuneration", "c": "It occurs in groups", "d": "It involves common goals"},
            "ca": "b"
            },

            #3-----------------------------
            {"question": "The qualities or characteristics typically belonging to a person that distinguishes him/her from other person is known as.",
            "answers": {"a": "Skills", "b": "Attitude", "c": "Traits", "d": "Style"},
            "ca": "c"
            },

            #4-----------------------------
            {"question": "The ability of a leader to share and understand the feelings of his/her followers is known as.",
            "answers": {"a": "Honesty", "b": "Conviction", "c": "Sympathy", "d": "Empathy"},
            "ca": "d"
            },

            #5-----------------------------
            {"question": "When a person becomes a leader of an organization by systems of convention, laws and regulations, we say that the leader's source of leadership is based on.",
            "answers": {"a": "Tradition", "b": "Inheritance", "c": "Charisma", "d": "Legal"},
            "ca": "d"
            },

            #6-----------------------------
            {"question": "A school head teacher who always masters his own environment with the goal of avoiding problems and always thinking 3 steps ahead is",
            "answers": {"a": "Adaptable", "b": "Reactive", "c": "Proactive", "d": "Open-minded"},
            "ca": "c"
            },


            #7-----------------------------
            {"question": "The ability to mobilize human and material resources towards achievement of organizational goals is known as.",
            "answers": {"a": "Coordinating", "b": "Administration", "c": "Management", "d": "Leadership"},
            "ca": "b"
            },

            #8-----------------------------
            {"question": "In a school situation when a head teacher influences his/her teachers because of their loyalty, respect and friendship, the head teacher is using.",
            "answers": {"a": "Referent power", "b": "Expert power", "c": "Coercive power", "d": "Legitimate power"},
            "ca": "a"
            },

            #9-----------------------------
            {"question": "Which one of the following is not a tangible reward?",
            "answers": {"a": "Recognition", "b": "Certificate", "c": "Plaques", "d": "Bonuses"},
            "ca": "a"
            },

            #10-----------------------------
            {"question": "When a head teacher decides in advance what to do, how to do and who is to do it, the head teacher is",
            "answers": {"a": "Establishing objectives", "b": "Planning", "c": "Supervising", "d": "Organising"},
            "ca": "b"
            },

            #11-----------------------------
            {"question": "The process of recruiting essential qualified teachers that will be responsible for teaching various subjects in a school is known as",
            "answers": {"a": "Directing", "b": "Coordinating", "c": "Staffing", "d": "Organising"},
            "ca": "c"
            },

            #12-----------------------------
            {"question": "In the school situation when a head teacher influences his/her teachers because of their loyalty, respect and friendship, the head teacher is using.",
            "answers": {"a": "Referent power", "b": "Expert power", "c": "Coercive power", "d": "Legitimate power"},
            "ca": "a"
            },

            #13-----------------------------
            {"question": "Which principle of organization states that every organization, big or small, must have clear lines of authority of communication from the top to the bottom and vice versa?",
            "answers": {"a": "Principles of authority", "b": "Principles of specialization", "c": "Principles of objectives", "d": "The Scalar Principles"},
            "ca": "d"
            },

            #14-----------------------------
            {"question": "At D/A basic school the head teacher and teachers are genuine in their behaviour and nothing is hidden from the staff. What type of school climate is the head teacher practising?",
            "answers": {"a": "Close but friendly Climate", "b": "Autonomous but controlled", "c": "Open Climate", "d": "Familiar climate"},
            "ca": "c"
            },

            #15-----------------------------
            {"question": "The Great Man theory assumes that:",
            "answers": {"a": "People are either born or made with certain qualities","b": "Traits of leadership are intrinsic","c": "Leaders are different from the average person", "d": "Successful leadership is based on definable and learnable behaviour"},
            "ca": "b"
            },

            #16-----------------------------
            {"question": "What type of leadership style is applied when a head teacher of a basic school adjust his/her style to fit the development level of the followers he/she is trying to influence.",
            "answers": {"a": "Situational Leadership", "b": "Transactional Leadership", "c": "Democratic Leadership", "d": "Transactional Lead"},
            "ca": "a"
            },

            #17-----------------------------
            {"question": "Which one of the following organizational theories is based on homogeneous set of culture characterized by homogeneity of values, beliefs and objectives?",
            "answers": {"a": "Theory Z", "b": "Theory Y", "c": "Theory X", "d": "Theory X and Z"},
            "ca": "a"
            },	

            #18-----------------------------           
            {"question": "This principle indicates that the success or failure of every organization largely depends on the handling of humans.",
            "answers": {"a": "Principles of balance", "b": "Principles of discipline", "c": "Principles of human element", "d": "Principles of supremacy"},
            "ca": "c"
            },
            
            #19-----------------------------
            {"question": "	One of the following factors does not promote intrinsic motivation",
            "answers": {"a": "Challenge", "b": "Salary", "c": "Trust", "d": "Recognition"},
            "ca": "b"
            },

            #20-----------------------------
            {"question": "The type of motivation where people show their feelings, behaviour and desire to help other people without selfishness or wanting something in return is referred to as",
            "answers": {"a": "Intrinsic motivation", "b": "Extrinsic motivation", "c": "Altruistic motivation", "d": "Internal motivation"},
            "ca": "c"
            },

            #21-----------------------------
            {"question": "According to Maslow, the physiological needs required to sustain life include.",
            "answers": {"a": "Air, Water, Food, Money", "b": "Water, Food, Sleep, Job security", "c": "Medical insurance, Air, Food, Water", "d": "Air, Food, Sleep, Water"},
            "ca": "d"
            },

            #22-----------------------------
            {"question": "The idea that all the units of an organization should be integrated under the authority of one- head had been interpreted as:",
            "answers": {"a": "Delegated legislation", "b": "Hierarchical system", "c": "Span of control", "d": "Unity of command"},
            "ca": "d"
            },

            #23-----------------------------
            {"question": "Managerial decision-making refers to:",
            "answers": {"a": "Information system", "b": "Operation research", "c": "Programmed decisions", "d": "Un-programmed decisions"},
            "ca": "c"
            },

            #24-----------------------------
            {"question": "Which one of the following is not a key function of a leader of an educational organization?",
            "answers": {"a": "Establishing direction", "b": "Influencing outcomes", "c": "Aligning people", "d": "Resolving conflict among staff"},
            "ca": "d"
            },

            #25-----------------------------
            {"question": "Schools can reach out to their various communities through all of the following except:",
            "answers": {"a": "Speech and Prize given days", "b": "Promotion of honour roll", "c": "Encouraging home visit", "d": "Teacher professionalism"},
            "ca": "d"
            },
            
            #26-----------------------------
            {"question": "In transformational leadership, the leader exhibits all the following elements except.",
            "answers": {"a": "Individualized Consideration", "b": "Intellectual stimulation", "c": "Ambiguity skills", "d": "Inspirational motivation"},
            "ca": "c"
            },

            #27-----------------------------
            {"question": "Which of the following techniques would be most likely to increase the motivation and satisfaction of teacher in a particular institution?",
            "answers": {"a": "Job enrichment", "b": "Job placement", "c": "Responsibility of workers", "d": "Satisfaction of workers"},
            "ca": "d"
            },


            #28-----------------------------
            {"question": "It is an approach in school administration where the leader appoints a small group of people to deal with specific problems.",
            "answers": {"a": "Committee of Inquiry", "b": "Open Committee", "c": "Referent Committee", "d": "Ad-hoc Committee"},
            "ca": "d"
            },

            #29-----------------------------
            {"question": "The communication process involves all of the following except one.",
            "answers": {"a": "Encoding", "b": "Decoding", "c": "Sender", "d": "Message"},
            "ca": "d"
            },

            #30-----------------------------
            {"question": "All of the following are examples of oral communication except one.",
            "answers": {"a": "Face-to-face conversation", "b": "Reports", "c": "Telephone conversation", "d": "Discussions"},
            "ca": "b"
            },

            #31-----------------------------
            {"question": "The function of management is putting into practice the policies and plans decided upon by the",
            "answers": {"a": "Administration", "b": "Manager", "c": "Production-team", "d": "Staff"},
            "ca": "a"
            },

            #32-----------------------------
            {"question": "All the following are examples of internal motivating esteem needs except one.",
            "answers": {"a": "Accomplishment", "b": "Reputation", "c": "Self-respect", "d": "Self-esteem"},
            "ca": "a"
            },
            
            #33-----------------------------
            {"question": "Which one of the following best describes participative leadership?",
            "answers": {"a": "Exhibiting personal concern for individuals or the group", "b": "Focusing on the tasks at hand, and letting the ends justify the means.", "c": "Giving specific direction, defining expectations, and assigning tasks to groups", "d": "Sharing information between management and the group and working together"},
            "ca": "d"
            },

            #34-----------------------------
            {"question": "All of the following statements are true about contingent reward except",
            "answers": {"a": "The leader provides material reward", "b": "The leader hardly punish staff who underperformed", "c": "The leader recognises good performance", "d": "The leader provides psychological rewards"},
            "ca": "b"
            }, 

            #35-----------------------------
            {"question": "When a basic school head teacher solves a problem unilaterally using the available information, he/she is using what type of decision-making style?",
            "answers": {"a": "Individual-consultative decision-making style", "b": "Autocratic decision-making style", "c": "Group-consultative decision-making style", "d": "Informed-autocratic decision-making style"},
            "ca": "b"
            },

            #36-----------------------------
            {"question": "Reporting function performed by administrators include all the following except.",
            "answers": {"a": "Keeping inventory of organization's properties", "b": "keeping records on staff", "c": "Discussing staff performance issues with stakeholders", "d": "administering and monitoring issues with stakeholders"},
            "ca": "d"
            },

            #37-----------------------------
            {"question": "Which one of the following is not a key function of a leader of an educational organization?",
            "answers": {"a": "Establishing direction", "b": "Influencing outcomes", "c": "Aligning people", "d": "Resolving conflict among staff"},
            "ca": "d"
            },

            #38-----------------------------
            {"question": "A leader may use or employ the laissez-fair style for all the following except ",
            "answers": {"a": "When staff members are highly matured as the leader", "b": "When staff members are highly experienced", "c": " When the leader wants to avoid performance-related confrontations", "d": "When staffs are self-directed"},
            "ca": "c"
            },

            #39-----------------------------
            {"question": "Barriers to effective school-community relations include all the following except",
            "answers": {"a": "Uncertainty of information", "b": "Lack of time", "c": " Lack of focus", "d": "Political influences"},
            "ca": "d"
            },

            #40-----------------------------
            {"question": "Which one of the following statements is untrue about theory Z?",
            "answers": {"a": "Promotion in organization is slow", "b": "Promotion in organization is rapid", "c": "Employees make special contributions", "d": "There is job security for employees"},
            "ca": "b"
            },

            #41-----------------------------
            {"question": " Decisions made without time to rehearse are known as?",
            "answers": {"a": "Strategic decisions", "b": "Operational decisions", "c": "Emergency decisions", "d": "Routine decisions"},
            "ca": "c"
            },
            
            
            #42-----------------------------
            {"question": "Which type of communication is 'minimally restricted' to individuals who engage in interpersonal communication and share some level of familiarity with each other??",
            "answers": {"a": "Oral Communication", "b": "Verbal Communication ", "c": "Interpersonal Communication", "d": "Non-verbal Communication"},
            "ca": "c"
            },

            #43-----------------------------
            {"question": "All of the following are examples of informal oral communication EXCEPT one.?",
            "answers": {"a": " Face-to-face  ", "b": "Presentations ", "c": "Classroom lectures", "d": "A speech at a graduation ceremony"},
            "ca": "a"
            },

            #44-----------------------------
            {"question": "One of the following is a disadvantage of written communication.?",
            "answers": {"a": "No need for personal contact", "b": "It saves money", "c": "It is a written proof", "d": "Lacks secrecy"},
            "ca": "d"
            },

            #45-----------------------------
            {"question": "Communication goes through all of the following steps EXCEPT.?",
            "answers": {"a": "Evaluation", "b": "Feedback", "c": "Encoding", "d": "Decoding"},
            "ca": "a"
            },

            #46-----------------------------
            {"question": "For effective communication to take place, the school leaders must do all of the following EXCEPT one.?",
            "answers": {"a": "Tell people", "b": "Find your voice", "c": "Be visible", "d": "Listen with your eyes and ears"},
            "ca": "a"
            },

            #47-----------------------------
            {"question": "By nature, decision-making comprises all of the following EXCEPT?",
            "answers": {"a": "A choice between alternatives", "b": "Selection of actions", "c": "Has an intended purpose", "d": "Made by only individuals"},
            "ca": "d"
            },

            #48-----------------------------
            {"question": "In the decision-making process individuals generate alternatives by doing one of the following.?",
            "answers": {"a": "By specifying the goals, he/she wants to achieve  ", "b": "By defining what the problem is and is not ", "c": "By identifying the impact, it will have on him/her self", "d": "By prioritizing the alternatives"},
            "ca": "a"
            },

            #49-----------------------------
            {"question": "Which one of the following stages in decision-making test for cause and effect?",
            "answers": {"a": "Generating alternatives", "b": "Identifying the problem", "c": "Evaluating the alternatives", "d": "Implementation"},
            "ca": "b"
            },

            #50-----------------------------
            {"question": "When a school head teacher makes a decision by sharing the problem with staff members and solicits their ideas without forming a group. What style of decision-making is he/she using?",
            "answers": {"a": "Informed-democratic decision-making", "b": "Group-consultative decision-making", "c": "Individual-consultative decision-making", "d": "Informed-autocratic decision-making"},
            "ca": "c"
            },

            #51-----------------------------
            {"question": "Clayton Alderfer's 'Growth' co-relates with Maslow's Need Hierarchy.?",
            "answers": {"a": "Self-actualization and external esteem needs", "b": "Internal esteem needs and Self actualization", "c": "Peak of fulfilment", "d": "Self-actualization and internal esteem needs"},
            "ca": "a"
            },

            #52-----------------------------
            {"question": "Which one of the following best describes a head teacher who has concern for his/her teachers that goes beyond the workplace?",
            "answers": {"a": "Moderately specialised concern", "b": "Informal concern", "c": "Holistic concern", "d": "Slow concern"},
            "ca": "c"
            },

            #53-----------------------------
            {"question": "One of the major differences between the ERG theory and Maslow's Need Hierarchy is",
            "answers": {"a": "The ERG theory does not acknowledge that when a higher need is frustrated, an individual may regress.", "b": "The ERG theory acknowledges that there is no difference in need preference between cultures than Maslow's Need Hierarchy", "c": "The ERG theory demonstrates that more than one need may motivate at the same time", "d": "Maslow's theory acknowledges that if a higher need is frustrated, an individual may regress to increase the satisfaction of a lower level need"},
            "ca": "c"
            },

            #54-----------------------------
            {"question": "Growth, according to the ERG theory refers to an intrinsic desire for ?",
            "answers": {"a": "Related needs  ", "b": "Growth needs ", "c": "Personal development", "d": "Interpersonal relationship"},
            "ca": "c"
            },

            #55-----------------------------
            {"question": "Maslow indicated that at the peak of fulfilment the self-actualized person's experiences.......?",
            "answers": {"a": "Profound happiness and harmony  ", "b": "Psychological growth ", "c": "Esteem harmony and truth", "d": "Self-respect and social status"},
            "ca": "a"
            },


            #56-----------------------------
            {"question": "One of the following is an assumption of theory Y.?",
            "answers": {"a": "Under no circumstance condition will people seek responsibilities  ", "b": "People are not self-directed to meet their work objectives ", "c": "Work cannot be as natural as play", "d": "People cam handle responsibility because there are creative"},
            "ca": "d"
            },

            #57-----------------------------
            {"question": "One of the criticisms of theory X is that ............?",
            "answers": {"a": "Once a need is satisfied it no longer motivate  ", "b": "It seeks for productivity rather than employee well-being ", "c": "Leaders are engaged in secluded form of multiplication", "d": "It lacks decentralization and job enlargement"},
            "ca": "a"
            },

            #58-----------------------------
            {"question": "What type of leadership style is practised when a head teacher passes along the day-to-day decision-making to his/her teachers?",
            "answers": {"a": "Delegating leadership  ", "b": "Participating leadership ", "c": "Telling leadership", "d": "Selling leadership"},
            "ca": "b"
            },

            #59-----------------------------
            {"question": "Which type of leadership style allows the head teacher to continually change his/her style to meet the needs of the teachers in the school?",
            "answers": {"a": "Situational leadership  ", "b": "Transformational leadership ", "c": "Transactional leadership", "d": "Participative leadership"},
            "ca": "a"
            },

            #60-----------------------------
            {"question": "Which leadership theory assumes that people are motivated by reward and punishment?",
            "answers": {"a": "Transactional leadership theory  ", "b": "Transformational leadership theory ", "c": "Situational leadership theory", "d": "Distributed leadership theory"},
            "ca": "a"
            },

            #61-----------------------------
            {"question": "Distributed leadership is premised on.....",
            "answers": {"a": "Loyalty and faith  ", "b": "Trust and honesty ", "c": "Honesty and faith", "d": "Trust and respect"},
            "ca": "d"
            },

            #62-----------------------------
            {"question": "The result of a leader's philosophy, personality and experience is known as his/her..........",
            "answers": {"a": "Leadership style  ", "b": "Leadership traits ", "c": "Leadership skills", "d": "Leadership qualities"},
            "ca": "a"
            },

            #63----------------------------
            {"question": "In which type of climate do we classify a head teacher who is ineffective in directing the activities of teachers and at the same time not inclined to look out for their well-being?",
            "answers": {"a": "Close climate  ", "b": "Open climate ", "c": "Both close and open", "d": "Paternal climate"},
            "ca": "a"
            },

            #64----------------------------
            {"question": "The type of school climate where the head teacher is dominant and directive is known as...............",
            "answers": {"a": "Open climate  ", "b": "Controlled climate ", "c": "Paternal climate", "d": "None of the above"},
            "ca": "b"
            },

            #65----------------------------
            {"question": "Which principle of organization stipulates that the success or failure of every organization depends on the handling of the employees and employers?",
            "answers": {"a": "Principle of human element  ", "b": "Principles of discipline ", "c": "Principle of balance", "d": "Principle of specialization"},
            "ca": "a"
            },

            #66----------------------------
            {"question": "In which type of organizational structure does authority flows downward from the top to the bottom.",
            "answers": {"a": "Matrix structure  ", "b": "Line structure ", "c": "Functional structure", "d": "Divisional structure"},
            "ca": "b"
            },

            #67----------------------------
            {"question": "The type of clique which consists of workers who are of similar rank in a school and who work in the same department is known as..................",
            "answers": {"a": "Mixed clique  ", "b": "Vertical clique ", "c": "Horizontal clique", "d": "None of the above"},
            "ca": "c"
            },


            #68-----------------------------
            {"question": "Paternal climates exist in a basic school..................",
            "answers": {"a": "Where teachers get little satisfaction with regards to their social needs  ", "b": "Where the head teacher listens to group suggestions but does not consider them ", "c": "Where the head teacher and teachers show friendliness", "d": "Where emphasis is one achievement at the expense of social satisfaction"},
            "ca": "b"
            },

            #69-----------------------------
            {"question": "In budgeting the head teacher does all the following activities except ..................",
            "answers": {"a": "Setting goals  ", "b": "Gathering information ", "c": "Amount of money and resources", "d": "Forecast future plans"},
            "ca": "c"
            },

            #70-----------------------------
            {"question": "The principle of staffing which states that teachers should be selected from among the best available candidates is known as ..................",
            "answers": {"a": "Principle of staff and universal development  ", "b": "Principle of open competition ", "c": "Principle of job recruitment", "d": "Principle of job definition"},
            "ca": "b"
            },

            #71-----------------------------
            {"question": "One amongst the following does not describe leadership ..................",
            "answers": {"a": "Organizations  ", "b": "Process ", "c": "Individual", "d": "Followers"},
            "ca": "a"
            },

            #72-----------------------------
            {"question": "Effective leadership is dependent on all EXCEPT one among the following:",
            "answers": {"a": "Setting  ", "b": "Context ", "c": "Environment", "d": "Management"},
            "ca": "d"
            },

            #73-----------------------------
            {"question": "In educational administration, the guidance, leadership and control of the efforts of a group of people towards some common objectives is ____",
            "answers": {"a": "Control  ", "b": "Leadership ", "c": "Management", "d": "Administration"},
            "ca": "c"
            },

            #74-----------------------------
            {"question": "Which of the following guru's propounded Theory Z?",
            "answers": {"a": "William Wuchi  ", "b": "William Ochi ", "c": "William Uchi", "d": "William Ouchi"},
            "ca": "d"
            },

            #75-----------------------------
            {"question": "Educational Leadership may include all EXCEPT one of the following:",
            "answers": {"a": "School setting  ", "b": "School Management ", "c": "PTA Management", "d": "School Records"},
            "ca": "c"
            },

            #76-----------------------------
            {"question": "The qualities or characteristics typically belonging to a person that distinguishes him/her from other person is known as ..................",
            "answers": {"a": "Skills  ", "b": "Attitude ", "c": "Traits", "d": "Style"},
            "ca": "c"
            },

            #77-----------------------------
            {"question": "A school head teacher who always masters his own environment with the goal of avoiding problems and always thinking 3 steps ahead is said to be a/an ..................",
            "answers": {"a": "Adaptable leader  ", "b": "Reactive leader ", "c": "Proactive leader", "d": "Open-minded leader"},
            "ca": "c"
            },

            #78-----------------------------
            {"question": "Decisions made without implementation are known as ..................",
            "answers": {"a": "Intentions  ", "b": "Strategic decisions ", "c": "Operational decisions", "d": "Emergency decisions"},
            "ca": "a"
            },

            #79-----------------------------
            {"question": "Why do autocratic leaders make decisions alone? Because ..................",
            "answers": {"a": "He/she has the right to do so  ", "b": "He/she is the strongest person in the group ", "c": "He/she has power centralised in him/her", "d": "He was born to do so"},
            "ca": "c"
            },

            #80-----------------------------
            {"question": "Under laissez-faire leadership, delegative style is generally not ..................",
            "answers": {"a": "Useful  ", "b": "Responsible ", "c": "Appropriate", "d": "Attractive"},
            "ca": "d"
            },

            #81-----------------------------
            {"question": "Which of the following is not considered a characteristic of planning functions?",
            "answers": {"a": "Planning is anticipatory  ", "b": "Planning is goal oriented ", "c": "Planning is future oriented", "d": "Planning is past oriented"},
            "ca": "d"
            },


            #82-----------------------------
            {"question": "Why are hierarchies not easily perceived in organisations under distributed leadership?",
            "answers": {"a": "leadership is distributed such that the people in the organisation care less about leadership  ", "b": "leadership is distributed such that the people in the organisation lead each other ", "c": "leadership is distributed such that the people in the organisation become law abiding", "d": "leadership is distributed such that the people in the organisation do not need a hierarchy"},
            "ca": "d"
            },

            #83----------------------------
            {"question": "Why should a leader not use one leadership style?",
            "answers": {"a": "Followers will take the leader for granted  ", "b": "Individual situations call for particular leadership style ", "c": "Followers will not obey the rules", "d": "To control individual situation and ensure compliance"},
            "ca": "b"
            },

            #84----------------------------
            {"question": "A school can reach its community through all the following means EXCEPT ____",
            "answers": {"a": "school magazines  ", "b": "organization of special event ", "c": "parent-teacher association", "d": "political rally"},
            "ca": "d"
            },

            #85----------------------------
            {"question": "Which one of the following is not considered to be a traditional leadership style?",
            "answers": {"a": "Authoritarian style  ", "b": "Coaching style ", "c": "Democratic style", "d": "Laissez-faire style"},
            "ca": "b"
            },

            #86----------------------------
            {"question": "A leader may employ the delegative style under all the following EXCEPT ____",
            "answers": {"a": "when followers are self-directed  ", "b": "when followers are self-motivated ", "c": "When followers are hight skilled", "d": "When followers work for reward"},
            "ca": "d"
            },

            #87----------------------------
            {"question": "All the following are physical features of a leaders according to the trait theory EXCEPT ____",
            "answers": {"a": "Ascendance  ", "b": "Appearance ", "c": "Height above average of peers", "d": "Weight above average of peers"},
            "ca": "a"
            },

            #88----------------------------
            {"question": "When a school and its community exist as separate entities, there is a/an ____",
            "answers": {"a": "cooperative system  ", "b": "closed system ", "c": "interpretation system", "d": "liberal system"},
            "ca": "b"
            },

            #89----------------------------
            {"question": "When a leader's task involves appointing school prefects, departmental heads and housemistress and assigning responsibilities and supporting them with the necessary resources for them to carry out such responsibilities he\she is said to be",
            "answers": {"a": "Planning  ", "b": "Organizing ", "c": "Staffing", "d": "Coordinating"},
            "ca": "c"
            },

            #90----------------------------
            {"question": "The process of taking the necessary preventive actions to ensure that an organization’s mission and objectives are accomplished refers to as",
            "answers": {"a": "Administration  ", "b": "Institution ", "c": "Management", "d": "Supervision"},
            "ca": "c"
            },

            #91----------------------------
            {"question": "This power of an administrator in an institution arises from the subordinate’s belief that the leader has the ability to punish them in a way that will prevent the satisfaction of a need.",
            "answers": {"a": "Reward power  ", "b": "Referent power ", "c": "Coercive power", "d": "Expert power"},
            "ca": "c"
            },

            #92----------------------------
            {"question": "All but one is not a characteristic of formal organization.",
            "answers": {"a": "Deliberately planned and created to achieve one or more long term goals", "b": "It is flexible and loosely structured ", "c": "Based on certain principles such as the specification of tasks", "d": "Concerns with the coordination of activities"},
            "ca": "b"
            },

            #93----------------------------
            {"question": "Why does informal organization develop to meet the needs ignored by the formal organization?",
            "answers": {"a": "Because it involves human needs to socialize  ", "b": "They do not have clear cut in their operation as formal organization ", "c": "The origins of informal organization are sometimes obscure", "d": "Bureaucracies turn to be impersonal, offering personal affection, support and human"},
            "ca": "a"
            },

            #94----------------------------
            {"question": "One activity associated with the directing function of management is",
            "answers": {"a": "Establishing goals  ", "b": "Determing tasks ", "c": "Instructing employees.", "d": "Interviewing applicants"},
            "ca": "b"
            },

            #95----------------------------
            {"question": "The rational decision making process can be seen as an ideal model because it is especially suitable in situations where",
            "answers": {"a": "There is a clear definition of the problem  ", "b": "Insufficient information is available. ", "c": "Divergent opinions are not tolerated.", "d": "The result is accepted by all."},
            "ca": "a"
            },
            
	    
        ]
        self.current_question_index = 0
        self.question_number = 1
        self.load_question()

    def load_question(self):
        if self.current_question_index >= len(self.questions):
            # Handle end of quiz (switch screens, etc.)
            return
        current_question = self.questions[self.current_question_index]
        self.question_text = current_question["question"]
        self.answer_a_text = current_question["answers"]["a"]
        self.answer_b_text = current_question["answers"]["b"]
        self.answer_c_text = current_question["answers"]["c"]
        self.answer_d_text = current_question["answers"]["d"]
        self.correct_answer = current_question["ca"]
        self.selected_answer = ""  # Reset selection on new question

    def check_answer(self, answer):
        self.selected_answer = answer
        # Change button color based on selection (green for correct, red for incorrect)
        if answer == self.correct_answer:
            self.ids[answer + "_btn"].background_color = (0, 1, 0, 1)  # Green
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (1, 1, 1, 1)
            self.ids[answer + "_btn"].theme_text_color = 'Custom'
        else:
            self.ids[answer + "_btn"].background_color = (1, 0, 0, 1)  # Red
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (1, 1, 1, 1)
            self.ids[answer + "_btn"].theme_text_color = 'Custom'
            #self.ids.a_btn.canvas.before.children[0].radius = [40]

    def next_question(self):
        
        if self.question_number < 95:
            self.current_question_index += 1
            self.question_number += 1 
            self.ids.question_number.text = f"{self.question_number}"
        elif self.question_number == 95:
            self.current_question_index += 0
            self.question_number = 95 
            self.ids.question_number.text = f"{self.question_number}"
        self.load_question()
        # Reset button colors to default for next question
        for answer in ("a", "b", "c", "d"):
            self.ids[answer + "_btn"].background_color = (.9,.9,1,.5)  # White
            self.ids[answer + "_btn"].background_normal = ''
            self.ids[answer + "_btn"].color = (0, 0, 0, 1)
            
    def previous_question(self):
        if self.question_number == 1:
            self.current_question_index -= 0
            self.question_number -= 0             
            self.ids.question_number.text = f"{self.question_number}"
            
            MDDialog( text = 'You can not go back!'
                
            )
        
        elif  self.question_number > 1:
            self.current_question_index -= 1
            self.question_number -= 1 
            self.ids.question_number.text = f"{self.question_number}"
        self.load_question()
        # Reset button colors to default for next question
        for answer in ("a", "b", "c", "d"):
            self.ids[answer + "_btn"].background_color = (.9,.9,1,.5)  # White
            self.ids[answer + "_btn"].color = (0, 0, 0, 1)

class TheUniversity(MDApp):
    def build(self):
        
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.accent_palette = 'Orange'
        self.theme_cls.primary_palette = 'Green'
        
        sm = ScreenManager()
        #sm.add_widget(WelcomeScreen(name = 'welcome_screen'))
        #sm.add_widget(LoginScreen(name = 'login_screen'))
        #sm.add_widget(SignupScreen(name = 'signup_screen'))
        sm.add_widget(HomeScreen(name = 'home_screen'))
        sm.add_widget(TrendsScreen(name = 'questions_screen'))
        sm.add_widget(PsychologyScreen(name = 'question'))
        
        return sm
        
if __name__ == '__main__':
    TheUniversity().run()