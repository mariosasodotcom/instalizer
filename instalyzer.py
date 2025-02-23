#!/usr/bin/env python3
# 
# GNU GENERAL PUBLIC LICENSE
# Version 5, 2025
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Author: mariosaso (Mario Saso)

import argparse
from bs4 import BeautifulSoup

class InstagramAnalyzer:
    """
    A class to analyze Instagram follower relationships from HTML files.
    
    This class extracts usernames from HTML files and computes:
        - Mutual followers
        - Users you follow who don't follow you back
        - Users who follow you but you don't follow them
    """
    
    def __init__(self, followers_file, following_file):
        """
        Initialize the analyzer with paths to the followers and following HTML files.
        
        :param followers_file: Path to the HTML file containing followers.
        :param following_file: Path to the HTML file containing following.
        """
        self.followers_file = followers_file
        self.following_file = following_file
        self.followers = set()
        self.following = set()
        self.mutual = set()
        self.not_following_back = set()
        self.not_followed_by = set()

    def extract_usernames_from_html(self, file_path):
        """
        Extracts usernames from an HTML file by parsing all <a> tags.
        
        :param file_path: Path to the HTML file.
        :return: A set of usernames extracted from the file.
        """
        usernames = set()
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                print(f"Processing file: {file_path}")
                soup = BeautifulSoup(file, "html.parser")
                for a in soup.find_all("a"):
                    text = a.get_text(strip=True)
                    if text:
                        usernames.add(text)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        return usernames

    def analyze(self):
        """
        Loads data from the followers and following HTML files and computes:
            - Mutual followers (intersection)
            - Users you follow who don't follow you back
            - Users who follow you but you don't follow them
        """
        print("Extracting followers...")
        self.followers = self.extract_usernames_from_html(self.followers_file)
        print(f"Found {len(self.followers)} followers.")

        print("Extracting following...")
        self.following = self.extract_usernames_from_html(self.following_file)
        print(f"Found {len(self.following)} following.")

        # Compute relationships
        self.mutual = self.followers & self.following
        self.not_following_back = self.following - self.followers
        self.not_followed_by = self.followers - self.following

    @staticmethod
    def save_usernames(usernames, file_path):
        """
        Saves a set of usernames to a text file, one per line.
        
        :param usernames: The set of usernames to save.
        :param file_path: The output file path.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            for username in sorted(usernames):
                file.write(username + "\n")
        print(f"Done! {len(usernames)} users saved in '{file_path}'.")

    def print_summary(self):
        """
        Prints summary statistics of the analysis.
        """
        print("\nSummary:")
        print(f"Mutual followers: {len(self.mutual)}")
        print(f"Users you follow who don't follow you back: {len(self.not_following_back)}")
        print(f"Users who follow you but you don't follow: {len(self.not_followed_by)}\n")


def main():
    """
    Main function to parse arguments and run the Instagram follower analysis.
    """
    parser = argparse.ArgumentParser(description="Instagram Follower Analyzer")
    parser.add_argument("-f", "--followers", required=True,
                        help="Path to HTML file with followers")
    parser.add_argument("-g", "--following", required=True,
                        help="Path to HTML file with following")

    args = parser.parse_args()

    # Create an instance of the analyzer with the provided file paths.
    analyzer = InstagramAnalyzer(args.followers, args.following)

    # Perform the analysis.
    analyzer.analyze()

    # Print a summary of the computed statistics.
    analyzer.print_summary()

    # Save the analysis results to text files.
    InstagramAnalyzer.save_usernames(analyzer.not_following_back, "not_following_back.txt")
    InstagramAnalyzer.save_usernames(analyzer.not_followed_by, "not_followed_by.txt")
    InstagramAnalyzer.save_usernames(analyzer.mutual, "mutual.txt")


if __name__ == "__main__":
    main()
