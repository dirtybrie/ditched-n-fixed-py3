# pw-crackers
# hashcrack.py
To use the script:<br/>
python -m pip install hashlib<br/>
cd /in/to/directory/pw-crackeers<br/>
python hashcrack.py<br/>
<br/>
This script only supports cracking MD5 hashes see the hashlib module at https://docs.python.org/3/library/hashlib.html<br/>
for adding other hashes to crack<br/>
<br />
1.You can practice with the templates privided -or-<br/>
2.Create your own MD5 Hash and Dictionary text.<br/>
<br/>
METHOD 1.<br/>
Password is Welcome<br/>
-Copy the hash in the welcome-md5.txt file and paste it to the hash entry<br/>
-Type in the path to file where the welcome.txt is created in this case<br/>
it's in the same directory type in welcome.txt<br/>
-And viola it worked!<br/>
<br/>
METHOD 2<br/>
Create your own md5hash and text<br/>
-$echo -n yourpassword | md5sum<br/>
-copy the hash for later or save the hash to a text file<br/>
-create a text file with how evermany lines of passwords you want as long<br/>
as it's not too big so you computer doesn't have a heart attack.<br/>
Also it's a simple script it doesn't have memory manipulation<br/>
ex:<br/>
  $echo -n whaaaaaatuup! | md5sum<br/>
  44a1819c9618be3c0001ae0f2bf010e9<br/>
  $touch password.txt<br/>
  $mousepad password.txt<br/>
  Put in whatever you want just be sure to include the password

![alt text](https://github.com/dirtybrie/ditched-n-fixed-py3/blob/base/pw-crakers/hashcrack.png?raw=true)
