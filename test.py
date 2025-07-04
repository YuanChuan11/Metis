import MySQLdb

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(
            host="192.168.108.133", 
            port=3306, 
            user="metis", 
            passwd="metis@123", 
            db="metis",
            charset='utf8'
        )
        print("连接成功！")
        
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"MySQL版本: {version}")
        
        conn.close()
    except Exception as e:
        print(f"连接失败: {e}")


