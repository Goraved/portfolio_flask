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
        'site_link': ['https://qa-skills.herokuapp.com/'],
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
    'qa_skills_bot': {
        'tech_name': 'qa_skills_bot',
        'index': '004',
        'title': 'QA Skills Bot',
        'desc': 'Telegram qa_skills_bot for the QA Skills project',
        'git_link': 'https://github.com/Goraved/qa_skills_bot',
        'site_link': ['https://t.me/qa_skills_bot'],
        'images': [
            {'name': 'qa_skills_bot_02.png', 'desc': 'Language comparisons'},
            {'name': 'qa_skills_bot_03.png', 'desc': 'Statistic by today'}
        ]
    },
    'typhon_web': {
        'tech_name': 'typhon_web',
        'index': '005',
        'title': 'Typhon Web UI',
        'desc': 'Basic test framework to test Web UI using Selenium + Page Object + Allure',
        'git_link': 'https://github.com/Goraved/Typhon-web-UI',
        'images': [
            {'name': 'typhon_web_02.png', 'desc': 'Selenium'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_api': {
        'tech_name': 'typhon_api',
        'index': '006',
        'title': 'Typhon API',
        'desc': 'Basic test framework to test REST API using requests + Allure',
        'git_link': 'https://github.com/Goraved/Typhon-API',
        'images': [
            {'name': 'typhon_api_02.png', 'desc': 'requests lib for the REST API'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_mobile': {
        'tech_name': 'typhon_mobile',
        'index': '007',
        'title': 'Typhon Mobile',
        'desc': 'Basic test framework to test Mobile UI using Appium + Page Object + Allure',
        'git_link': 'https://github.com/Goraved/Typhon-Mobile',
        'images': [
            {'name': 'typhon_mobile_02.png', 'desc': 'Appium'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
    'typhon_ubuntu': {
        'tech_name': 'typhon_ubuntu',
        'index': '008',
        'title': 'Typhon Ubuntu',
        'desc': 'Basic test framework to test Ubuntu',
        'git_link': 'https://github.com/Goraved/Typhon-Ubuntu',
        'images': [
            {'name': 'typhon_ubuntu_02.png', 'desc': 'Ubuntu'},
            {'name': 'allure_icon.png', 'desc': 'Allure'}
        ]
    },
}
PROJECT_LINKS = [{'link': PROJECTS[project]['tech_name'], 'index': PROJECTS[project]['index']} for project in PROJECTS]
