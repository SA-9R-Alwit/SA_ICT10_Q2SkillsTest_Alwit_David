from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "math": {
                "name": "Math Club",
                "description": "A club for math enthusiasts of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 221",
                "advisor": "Ms. Lim",
                "members": 20,
                "category": "Academic"
            },
            "science": {
                "name": "Science Club",
                "description": "For students interested in science.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Science Lab",
                "advisor": "Mr. Lucena",
                "members": 22,
                "category": "Academic"
            },
            "glee": {
                "name": "Glee Club",
                "description": "For people who love singing.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Music Room",
                "advisor": "Ms. Llanes",
                "members": 18,
                "category": "Arts"
            },
            "commarts": {
                "name": "Commarts Club",
                "description": "Develop public speaking and argumentation skills.",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Room 211",
                "advisor": "Ms. Cantona",
                "members": 12,
                "category": "Academic"
            },
            "cocc": {
                "name": "COCC",
                "description": "Get trained to become a cadet officer.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Room 214",
                "advisor": "Ms. Mobilia",
                "members": 20,
                "category": "Arts"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")