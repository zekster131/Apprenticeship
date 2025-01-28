https://mystery.knightlab.com/

-- NOTE: for all of the "SELECT *" you could narrow it down and get the values like "SELECT interview_transcript", but I like to select all to see everything going on

Statements:
SELECT * from crime_scene_report -- Checking format of the table
  
SELECT * from crime_scene_report where date = 20180115 and type = "murder" and city = "SQL City" -- Checking conditions for: you vaguely remember that the crime was a ​murder​ that occurred sometime on ​Jan.15, 2018​ and that it took place in ​SQL City​.
  -- Output: Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".
  
SELECT *, max(address_number) from person where address_street_name = "Northwestern Dr" -- Identifies the highest number (last) house on Northwestern Dr using max()
  
SELECT * from person where address_street_name = "Franklin Ave" and name like "Annabel%" -- Checking for people on Franklin Ave with 'Annabel' as their first name
  
SELECT * from interview -- Checking format of the table
  
SELECT * from interview where person_id in (14887, 16371) -- Checks for both witnesses' transcripts
  
SELECT * from get_fit_now_check_in where check_in_date = 20180109 and membership_id like "48Z%" -- Checking for the 'number on the bag' and who checked in on the 9th Jan 2018
  
SELECT * from get_fit_now_member where id like "48Z%" -- Getting names and membership status for members with an id that starts with '48Z'
  
SELECT * from get_fit_now_member where id like "48Z%" and membership_status = "gold" -- Narrowing down to 2 suspects as 'only gold members have those bags'
  
SELECT * from person where id in (28819, 67318) -- Finding general information about the suspects

// THIS IS A SKIP I ACCIDENTALLY FOUND //
SELECT * from interview where person_id in (28819, 67318)
SELECT * from person where id = 67318
//

-- Assuming we completely trust the witnesses (especially witness 1) --
SELECT * from drivers_license where id in (173289, 423327) and plate_number like "%H42W%" -- Finding, out of the two suspects, which one has a license plate with 'H42W' in
-- Outputs Jeremy Bowers' information --
INSERT INTO solution VALUES (1, 'Jeremy Bowers'); -- Confirming the murderer is Jeremy Bowers and it is!
SELECT value FROM solution;

-- Output: Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge, try querying the interview 
-- transcript of the murderer to find the real villain behind this crime. If you feel especially confident in your SQL skills,
-- try to complete this final step with no more than 2 queries. Use this same INSERT statement with your new suspect to check your answer.

SELECT * from interview where person_id = 67318 -- Selecting the transcript from the murderer's interview

SELECT * from drivers_license where hair_color = "red" and gender = "female" and car_make = "Tesla" and height between 65 and 67 -- Checking for the conditions contained in Jeremy's transcript; 3 suspects
SELECT * from person where license_id in (202298, 291182, 918773) -- Gathering the 3 suspect's general information

SELECT * from facebook_event_checkin where event_name = "SQL Symphony Concert" and date like "%201712%" and person_id in (78881, 90700, 99716) -- Checking which ones have been to the concert 3 times in december, 
SELECT * from person where id = 99716 -- Check who id 99716 is as they were outputted 3 times
-- Outputs Miranda Priestly's information -- 
  
INSERT INTO solution VALUES (1, 'Miranda Priestly'); -- Confirming the real villain is Miranda Priestly and it is!
SELECT value FROM solution;

-- INFORMATION -- 

/*
crime report
date: 20180115
type: murder
description: Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".
city: SQL City

witness 1
name: Morty Schapiro
person_id: 14887
license_id: 118009
address_number: 4919
address_street_name: Northwestern Dr
ssn: 111564949
interview_transcript: I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".


witness 2
name: Annabel Miller
person_id: 16371
license_id: 490173
address_number: 103
address_street_name: Franklin Ave
ssn: 318771143
interview_transcript: I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

suspect 1
name: Joe Germuska
person_id: 28819
license_id: 173289
address_number: 111
address_street_name: Fisk Rd
ssn: 138909730
membership_start_date: 20160305
membership_status: gold
membership_id: 48Z7A
check_in_date: 20180109
check_in_time: 1600
check_out_time: 1730

suspect 2
name: Jeremy Bowers
person_id: 67318
license_id: 423327
address_number: 530
address_street_name: Washington Pl, Apt 3A
ssn: 871539279
membership_start_date: 20160305
membership_status: gold
membership_id: 48Z55
check_in_date: 20180109
check_in_time: 1530
check_out_time: 1700

MURDERER:
Jeremy Bowers
I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.
  
REAL VILLAIN:
Miranda Priestly
*/

