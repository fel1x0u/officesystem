class Envs:
    def __init__(self, *args, **kwargs):
        self.creds = {
    "admin": {
        "privs": 2,
        "password": "securepassword"
    },
    "root": {
            "privs": 3,
            "password": "toor"
    },
    "felix": {
        "privs": 2,
        "password": "So5327048"
    },
        "regularuser": {
            "privs": 1,
            "password": "hello"

        },
        "testing": {
            "privs": 3,
                "password": "t"
            },
            "nothing": {
            "privs": 0,
            "password": "123"
    },
    "noneedformetohaveapassword": {
        "privs": 0,
        "password": " ",
        "reason": "I am a low privilaged user"
    },
    "stephenou": {
        "privs": 2,
        "password": "So5327048"
    }
}
