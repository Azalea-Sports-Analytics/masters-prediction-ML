"""

Using that is formatted like the data for "data\masters-com-data\extract-2024.json" and "data\masters-com-data\extract-2023.json",
create a process to convert into a csv

Within the csv I want the following columns
- Year (i.e 2023, 2024)
- player id
- round number (1,2,3,4)
- hole number (1,2,3,...,17,18)
- hole score 

Below is how one player's data looks like in the 
"player": [
            {
                "id": "46046",
                "display_name": "SCHEFFLER",
                "display_name2": "Scheffler",
                "first_name": "Scottie",
                "last_name": "Scheffler",
                "full_name": "Scottie Scheffler",
                "countryName": "United States",
                "countryCode": "USA",
                "live": "",
                "video": false,
                "pos": "1",
                "image": true,
                "amateur": false,
                "past": true,
                "firsttimer": false,
                "status": "F",
                "newStatus": "F4",
                "active": false,
                "us": true,
                "intl": false,
                "teetime": "2:35 PM",
                "epoch": 1713119700,
                "tee_order": "59",
                "sort_order": "2|3|1|1",
                "start": "SAAAA",
                "group": "30",
                "today": "-4",
                "thru": "F",
                "groupHistory": "14|29|29|30",
                "thruHistory": "18|18|18|18",
                "lastHoleWithShot": "4|18",
                "holeProgress": 4,
                "topar": "-11",
                "total": "277",
                "totalUnderPar": "true",
                "movement": "0",
                "last_highlight": "2024_r4_46046_18_4",
                "round1": {
                    "prior": null,
                    "fantasy": 24,
                    "total": 66,
                    "roundStatus": "Finished",
                    "scores": [
                        4,
                        4,
                        4,
                        3,
                        4,
                        2,
                        4,
                        5,
                        4,
                        4,
                        4,
                        2,
                        4,
                        4,
                        4,
                        2,
                        4,
                        4
                    ]
                },
                "round2": {
                    "prior": -6,
                    "fantasy": 15,
                    "total": 72,
                    "roundStatus": "Finished",
                    "scores": [
                        4,
                        4,
                        4,
                        3,
                        5,
                        3,
                        5,
                        4,
                        4,
                        3,
                        4,
                        3,
                        6,
                        4,
                        5,
                        3,
                        4,
                        4
                    ]
                },
                "round3": {
                    "prior": -6,
                    "fantasy": 16,
                    "total": 71,
                    "roundStatus": "Finished",
                    "scores": [
                        3,
                        5,
                        3,
                        4,
                        4,
                        3,
                        4,
                        5,
                        4,
                        6,
                        5,
                        3,
                        3,
                        4,
                        4,
                        3,
                        5,
                        3
                    ]
                },
                "round4": {
                    "prior": -7,
                    "fantasy": 19,
                    "total": 68,
                    "roundStatus": "Finished",
                    "scores": [
                        4,
                        5,
                        3,
                        4,
                        4,
                        3,
                        5,
                        4,
                        3,
                        3,
                        5,
                        3,
                        4,
                        3,
                        5,
                        2,
                        4,
                        4
                    ]
                }
            },


    For illustrative purposes I have got one player's data from the extract-2024.json 
    The scores: shows the 18 hole scores that I would want converted to track the hole number and the score 
"""