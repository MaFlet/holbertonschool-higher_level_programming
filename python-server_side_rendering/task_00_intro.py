#!/usr/bin/python3
"""This Script is used to generate invitations"""
import os

def generate_invitations(template, attendees):
    """Function to generate invitations"""
    try:
        if not isinstance(template, str):
            print("Error: Invalid input - template must be a string")
            return []
        if not template.strip():
            print("Template is empty, no output files generated.")
            return []
        
        if not isinstance(attendees, list):
            print("Error: Invalid input - attendees must be a list")
            return []
        if not attendees:
            print("No data provided, no ouput files generated.")
            return []
        if not all(isinstance(a, dict) for a in attendees):
            print("Error: Each attendee must be a dictionary")
            return []
    
        invitations = []
        for index, attendee in enumerate(attendees, 1):
            try:
                invitation = template 

                invitation = invitation.replace("{name}", attendee.get('name', 'N/A'))
                invitation = invitation.replace("{event_title}", attendee.get('event_title', 'N/A'))
                invitation = invitation.replace("{event_date}", attendee.get('event_date', 'N/A'))
                invitation = invitation.replace("{event_location}", attendee.get('event_location', 'N/A'))

                filename = f"ouput_{index}.txt"

                if os.path.exists(filename):
                    print(f"Warning: {filename} already exists, overwriting...")

                try:
                    with open(filename, 'w') as file:
                        file.write(invitation)
                        print(f"Successfully created {filename}")
                except IOError as e:
                    print(f"Error: Could not write to {filename}: {e}")
                    continue

                invitations.append(invitation)

            except Exception as e:
                print(f"Warning: Error processing attendee {index}: {e}")
                return []
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
        return []
    return invitations
