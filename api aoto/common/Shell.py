import subprocess
import allure_pytest
import allure


class Shell:
    @staticmethod
    def invoke(cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, stderr = process.communicate()
        o = output.decode("gbk")
        e = stderr.decode("gbk")
        print("[out]\n", o)
        print("[err]\n", e)
        return o, e

    @staticmethod
    def run():
        process = subprocess.Popen(['ipconfig'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        output, stderr = process.communicate()
        o = output.decode("gbk")
        e = stderr.decode("gbk")
        print("[out]\n", o)
        print("[err]\n", e)
        return o, e


if __name__ == "__main__":
    s = Shell()
    s.run()
