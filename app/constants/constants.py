SECONDS_PER_DAY = 60*60*24
FIRST_TIME_VISIT_COOKIE_EXPIRES_AFTER = SECONDS_PER_DAY
MAX_REPOS_IN_GET_QUERY = 50
GITHUB_USERNAME = 'frankie-engineer'
GOOGLE_CLOUD_CONSOLE_BUCKET_NAME = 'portfolio-videos'

PAGES = { 
    'Home': '/',
    'Highlights' : '/highlights',
    'More' : '/more',
}

HEADER_ICON_BUTTONS = [
    {
        'name': 'LinkedIn',
        'url': 'https://www.linkedin.com/in/frankie-willcox-esparza/',
        'icon': 'fa-brands fa-linkedin'
    },
    {
        'name': 'Github',
        'url': 'https://github.com/frankie-engineer',
        'icon': 'fa-brands fa-github'
    },
    {
        'name': 'Download Resume',
        'url': '',
        'icon': 'fa-regular fa-file'
    },
    {
        'name': 'Email Me',
        'url': 'https://mail.google.com/mail/u/0/?fs=1&to=fwesparza@gmail.com&tf=cm',
        'icon': 'fa fa-envelope'
    }
]

TOPICS = {
   'Full-stack': '/more/?topic=postgresql',
   'React' : '/more/?topic=react',
   'Flask': '/more/?topic=flask',
   'Back-end': '/more/?topic=sql',
   'Data Structures & Algorithms': '/more/?topic=data-structures&topic=algorithms'
}