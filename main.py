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
        authorization_json = self.clubhouse.complete_phone_number_auth(phone_num, verification_code)
        user_id = authorization_json['user_profile']['user_id']
        user_token = authorization_json['auth_token']
        self.clubhouse.__init__(user_id, user_token)

    def get_followers(self, account_id):
        a = self.clubhouse.get_followers(account_id, page_size=50, page=1)
        print(f'Get followers\n{a}')
        return a

    def get_user_id(self, username):
        a = self.clubhouse.search_users(username)
        print(f'Get user\n{a}')
        return a

    def scrape_followers(self, username, csv_filename='output.csv', json_filename='output.json'):
        account_id = self.get_user_id(username)
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
    searched_user_id = input('Enter the username to scrape followers: ')
    c.scrape_followers(searched_user_id)
