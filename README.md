# **Instalyzer**  
**Analyze your Instagram followers and following lists from HTML files.**  

This tool extracts usernames from **Instagram data downloads** and determines:  
✔️ **Mutual Followers**  
✔️ **Users You Follow Who Don't Follow You Back**  
✔️ **Users Who Follow You But You Don't Follow**  

---

## **License**  
This project is licensed under the **GNU General Public License v3**.  
See [LICENSE](https://www.gnu.org/licenses/) for details.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/mariosasodotcom/instalyzer.git
cd instalyzer
```

### **2. Install Dependencies**  
Use `pip` to install the required libraries:  
```bash
pip install -r requirements.txt
```
or manually:  
```bash
pip install beautifulsoup4
```

---

## **How to Get Your Instagram Data**  
1. Tap on the **three lines** at the **top right** of your profile.  
2. Select **Your Activity**.  
3. Scroll down and tap **Download Your Information**.  
4. Tap **Request Download**.  
5. Tap **Select Types of Information**.  
6. Check **Followers and Followings**.  
7. Change **Date Range** to **All Time**.  
8. Submit your request.  

You'll receive the files in the same **Download Your Information** page after **15-20 minutes**.  

Once the download is ready:  
- Extract the ZIP file.  
- Locate `followers.html` and `following.html`.  

---

## **Usage**  

### **Run Instalyzer**  
```bash
python instalyzer.py -f followers.html -g following.html
```
The script will **automatically generate and save** the following files:  
- `not_following_back.txt` → Users you follow, but they don’t follow you back.  
- `not_followed_by.txt` → Users who follow you, but you don’t follow them.  
- `mutual.txt` → Users you follow and who follow you back.  

### **Example Output**  
```
Processing file: followers_1.html
Found 120 followers.
Processing file: following.html
Found 180 following.

Summary:
Mutual followers: 95
Users you follow who don't follow you back: 85
Users who follow you but you don't follow: 25

Done! 85 users saved in 'not_following_back.txt'.
Done! 25 users saved in 'not_followed_by.txt'.
Done! 95 users saved in 'mutual.txt'.
```

---

## **Features**  
✅ **No API Key Required** – Works entirely offline using HTML files.  
✅ **Fast and Simple** – Processes data in seconds.  
✅ **Automated File Output** – Saves results into organized text files.  
✅ **Verbose Mode Always On** – Prints real-time processing details.  
  
