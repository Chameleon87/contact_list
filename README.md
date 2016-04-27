# contact_list
Felt like I needed to brush up on my fundamentals so I made a contact list where you can add contacts and see a list of all the contacts... Still figuring out how to send and receive data from using a text file as a database... pretty interesting stuff.

So far you have the following modules and their uses:
<ul>
    <li>Phone Number.py - This is your main module that has all of the other modules imported, it also contains all of your main functions:
        <ul>
            <li>Start() - Starts the application and questions whether you would like to see all of the current contacts you've saved to your contact_list.txt file</li>
            <li>new_contact_first_name() - Goes through the step by step process of being able to add a first name to the contact and verify that it's the name you're wanting to add, it also automatically capitalizes the first name.</li>
            <li>new_contact_last_name() - Goes through the step by step process of being able to add a last name to the contact and verify that it's the name you're wanting to add, also automatically capitalizes the proper name.</li>
            <li>new_contact_phone_number() - Step by step to add a phone number to that contact and ends by saving the data into a pickle.dump into a contact_list.txt file for future extraction.</li>
        </ul>
    </li>
    <li>Models.py - That currently stores the Contact class that basically holds the "routing" links for the contact file to pull up all current contacts saved to it and the def of a Contact.</li>
</ul>

As it grows in complication I'll add more modules and functionality.

I have to create a contact_list model and move the methods on Contact to it... a few more changes and it will be functional.
