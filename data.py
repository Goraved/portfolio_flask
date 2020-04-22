PROJECTS = {
    'aqa_topics': {
        'tech_name': 'aqa_topics',
        'index': '001',
        'title': 'AQA Topics',
        'desc': 'Pet project to share knowledges between AQA engineers.\n Basically, it\'s a storage for the interesting topics for the QA Automation engineers',
        'git_link': 'https://github.com/Goraved/AQA_topics',
        'site_link': ['https://aqa-topics.herokuapp.com/'],
        'images': [
            {'name': 'aqa_topics_02.png', 'desc': 'Search page'},
            {'name': 'aqa_topics_03.png', 'desc': 'Admin page'}
        ]
    },
    'qa_skills': {
        'tech_name': 'qa_skills',
        'index': '002',
        'title': 'QA Skills',
        'desc': 'Pet project to gather all vacancies from Dou.ua, analyze them and make statistics by skills',
        'git_link': 'https://github.com/Goraved/qa_skills',
        'site_link': ['https://qa_skills.herokuapp.com/'],
        'images': [
            {'name': 'qa_skills_02.png', 'desc': 'Statistic by day'},
            {'name': 'qa_skills_03.png', 'desc': 'Statistic by skill'}
        ]
    },
    'sbt': {
        'tech_name': 'sbt',
        'index': '003',
        'title': 'SBT rehearsals',
        'desc': 'Just a site for manage rehearsals schedule of band SBT',
        'git_link': 'https://github.com/Goraved/dodiki',
        'site_link': ['https://dodiki.herokuapp.com/'],
        'images': [
            {'name': 'sbt_02.png', 'desc': 'Rehearsals list'},
            {'name': 'sbt_03.png', 'desc': 'Reschedule'}
        ]
    },
    'typhon_web': {
        'tech_name': 'typhon_web',
        'index': '004',
        'title': 'Typhon Web UI',
        'desc': 'Basic test framework to test Web UI using Selenium + Page Object + Allure',
        'git_link': 'https://github.com/Goraved/typhon_web',
        'images': [
            {'name': 'typhon_web_02.png', 'desc': 'Selenium'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_api': {
        'tech_name': 'typhon_api',
        'index': '005',
        'title': 'Typhon Web API',
        'desc': 'Basic test framework to test REST API using requests + Allure',
        'git_link': 'https://github.com/Goraved/typhon_web',
        'images': [
            {'name': 'typhon_api_02.png', 'desc': 'requests lib for the REST API'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_mobile': {
        'tech_name': 'typhon_mobile',
        'index': '006',
        'title': 'Typhon Mobile',
        'desc': 'Basic test framework to test Mobile UI using Appium + Page Object + Allure',
        'git_link': 'https://github.com/Goraved/typhon_mobile',
        'images': [
            {'name': 'typhon_mobile_02.png', 'desc': 'Appium'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_ubuntu': {
        'tech_name': 'typhon_ubuntu',
        'index': '007',
        'title': 'Typhon Ubuntu',
        'desc': 'Basic test framework to test Ubuntu',
        'git_link': 'https://github.com/Goraved/typhon_ubuntu',
        'images': [
            {'name': 'typhon_ubuntu_02.png', 'desc': 'Ubuntu'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
}
PROJECT_LINKS = [{'link': PROJECTS[project]['tech_name'], 'index': PROJECTS[project]['index']} for project in PROJECTS]
