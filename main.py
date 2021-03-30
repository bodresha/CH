import csv
import json

from clubhouse.clubhouse import Clubhouse


class FollowersIDScraper:
    def __init__(self):
        self.clubhouse = Clubhouse()

    def login(self):
        phone_num = input('Enter your phone number: ')
        self.clubhouse.start_phone_number_auth(phone_num)
        self.clubhouse.call_phone_number_auth(phone_num)
        verification_code = input('Enter the code you received: ')
        a = self.clubhouse.complete_phone_number_auth(phone_num, verification_code)
        return a

    def get_followers(self, account_id):
        return self.clubhouse.get_followers(account_id, page_size=500, page=1)

    def scrape_followers(self, account_id, csv_filename='output.csv', json_filename='output.json'):
        followers = self.get_followers(account_id)
        with open(csv_filename, 'a+') as csv_file:
            writer = csv.writer(csv_file)
            for follower in followers:
                writer.writerow([follower])
        print(f'Finished adding followers to {csv_filename}')

        with open(json_filename, 'a+') as json_file:
            for follower in followers:
                json.dump(follower, json_file)
        print(f'Finished adding followers to {json_filename}')


if __name__ == '__main__':
    c = FollowersIDScraper()
    c.login()
    user_id = input('Enter the user id of the user: ')
    c.scrape_followers(user_id)
