import subprocess
import sys
import os

def run_attack():
    """
    এই ফাংশনটি attack.py ফাইলটি রান করাবে
    """
    try:
        # চেক করা attack.py ফাইলটি আছে কিনা
        if not os.path.exists("attack.py"):
            print("\033[91m[!] ERROR: attack.py ফাইলটি পাওয়া যায়নি!\033[0m")
            print("\033[93m[!] নিশ্চিত করুন যে attack.py ফাইলটি একই ডিরেক্টরিতে আছে\033[0m")
            return False
        
        print("\033[92m[+] attack.py রান করা হচ্ছে...\033[0m")
        print("-" * 50)
        
        # attack.py রান করা
        result = subprocess.run([sys.executable, "attack.py"], 
                              capture_output=False, 
                              text=True)
        
        if result.returncode == 0:
            print("\n\033[92m[✓] attack.py সফলভাবে সম্পন্ন হয়েছে!\033[0m")
        else:
            print("\n\033[91m[✗] attack.py তে ত্রুটি হয়েছে!\033[0m")
            
        return result.returncode == 0
        
    except FileNotFoundError:
        print("\033[91m[!] ERROR: Python পাওয়া যায়নি!\033[0m")
        return False
    except Exception as e:
        print(f"\033[91m[!] একটি ত্রুটি ঘটেছে: {e}\033[0m")
        return False

def run_with_args(*args):
    """
    আর্গুমেন্টসহ attack.py রান করার জন্য (যদি প্রয়োজন হয়)
    """
    try:
        if not os.path.exists("attack.py"):
            print("\033[91m[!] ERROR: attack.py ফাইলটি পাওয়া যায়নি!\033[0m")
            return False
        
        cmd = [sys.executable, "attack.py"] + list(args)
        result = subprocess.run(cmd, capture_output=False, text=True)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"\033[91m[!] ত্রুটি: {e}\033[0m")
        return False

if __name__ == "__main__":
    # ক্লিয়ার স্ক্রিন
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[96m" + "=" * 50)
    print("         LOADER - attack.py এক্সিকিউটর")
    print("=" * 50 + "\033[0m")
    
    # সাধারণভাবে attack.py রান করা
    run_attack()
    
    # যদি আর্গুমেন্ট দিতে চান (আনকমেন্ট করুন):
    # run_with_args("--target", "example.com")
