query = """CALL list_all_invitedto_and_hosted_events(%s)"""
        mycursor.execute(query, (username,), multi=True)
        for result in mycursor:
            print("An INVITE!")
            allEvents = result.fetchall()  # Fetch rows for the current result set
            for event in allEvents:
                eventID, name, day, time = event
                print(eventID, name, day, time)
                self.myEvents(name, day, time, eventID)