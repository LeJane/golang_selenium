#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#QQ:29295842  希望大家多多来交流
#QQ:29295842  希望大家多多来交流
import os
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import sys,os
import socket
from StringIO import StringIO
import base64
import zipfile
import time
from PIL import Image    #图片编辑
import string
import re
#import base64
import uncrypt_decrypt
import SendKeys
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
debug=True    #是否开启调试
#base64.b64encode(s)  编码
#base64.b64decode(a)   解码

#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，
    #如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def web_close():  #结束浏览器
    try:
        os.system('taskkill /f /t /im chrome.exe')
        os.system('taskkill /f /t /im chromedriver.exe')
    except Exception as err:
        pass

def send_Keys(name):
    if name=="NULL":
        return Keys.NULL
    if name=="CANCEL":
        return Keys.CANCEL  # ^break
    if name=="HELP":
        return Keys.HELP
    if name=="BACKSPACE" or name=="BACK_SPACE":  #删除键
        return Keys.BACKSPACE
    if name=="TAB":
        return Keys.TAB   #TAB键
    if name=="CLEAR":
        return Keys.CLEAR
    if name=="RETURN":
        return Keys.RETURN
    if name=="ENTER":
        return Keys.ENTER   #回车键
    if name=="SHIFT" or name=="LEFT_SHIFT":
        return Keys.SHIFT  #Shift键
    if name=="CONTROL" or name=="LEFT_CONTROL":#Ctrl 键
        return Keys.CONTROL
    if name=="ALT" or name=="LEFT_ALT":
        return Keys.ALT          #Alt 键
    if name=="PAUSE":
        return Keys.PAUSE
    if name=="ESCAPE":
        return Keys.ESCAPE   #ECS键
    if name=="SPACE":
        return Keys.SPACE    #空格键
    if name=="PAGE_UP":
        return Keys.PAGE_UP   #PgUp 键
    if name=="PAGE_DOWN":
        return Keys.PAGE_DOWN  #PgDwon 键
    if name=="END":
        return Keys.END     #END 键
    if name=="HOME":
        return Keys.HOME    #HOME 键
    if name=="LEFT" or name=="ARROW_LEFT":
        return Keys.LEFT  #左键
    if name=="UP" or name=="ARROW_UP":
        return Keys.UP     #上键
    if name=="RIGHT" or name=="ARROW_RIGHT":  #右键
        return Keys.RIGHT
    if name=="DOWN" or name=="ARROW_DOWN":
        return Keys.DOWN       #下键
    if name=="INSERT":
        return Keys.INSERT    #insert键
    if name=="DELETE":
        return Keys.DELETE     #del键

    if name=="":
        return Keys.SEMICOLON   #';'键
    if name=="":
        return Keys.EQUALS     #'='键
    #数字键盘
    if name=="NUMPAD0":
        return Keys.NUMPAD0   # number pad keys
    if name=="NUMPAD1":
        return Keys.NUMPAD1
    if name=="NUMPAD2":
        return Keys.NUMPAD2
    if name=="NUMPAD3":
        return Keys.NUMPAD3
    if name=="NUMPAD4":
        return Keys.NUMPAD4
    if name=="NUMPAD5":
        return Keys.NUMPAD5
    if name=="NUMPAD6":
        return Keys.NUMPAD6
    if name=="NUMPAD7":
        return Keys.NUMPAD7
    if name=="NUMPAD8":
        return Keys.NUMPAD8
    if name=="NUMPAD9":
        return Keys.NUMPAD9
    if name=="MULTIPLY":
        return Keys.MULTIPLY  # '*' 键
    if name=="ADD":
        return Keys.ADD    # '+' 键
    if name=="SEPARATOR":
        return Keys.SEPARATOR   #','键
    if name=="SUBTRACT":
        return Keys.SUBTRACT   # '-' 键
    if name=="DECIMAL":
        return Keys.DECIMAL    # '.'键
    if name=="DIVIDE":
        return Keys.DIVIDE     #'/'键

    if name=="F1":
        return Keys.F1  # function  keys
    if name=="F2":
        return Keys.F2
    if name=="F3":
        return Keys.F3
    if name=="F4":
        return Keys.F4
    if name=="F5":
        return Keys.F5
    if name=="F6":
        return Keys.F6
    if name=="F7":
        return Keys.F7
    if name=="F8":
        return Keys.F8
    if name=="F9":
        return Keys.F9
    if name=="F10":
        return Keys.F10
    if name=="F11":
        return Keys.F11
    if name=="F12":
        return Keys.F12

    if name=="META":
        return Keys.META
    if name=="COMMAND":
        return Keys.COMMAND
    return ""




class css_selenium(object):
    # def __init__(self):
    #     self.browser=None  #全局控制
    #     self.executable_path = cur_file_dir()+"\Chrome\chromedriver.exe"
    #     os.environ["webdriver.chrome.driver"] = self.executable_path
    #     self.options = webdriver.ChromeOptions()
    #     self.options.add_argument('disable-infobars')
    #     #prefs = {"--disable-bundled-ppapi-flash": 2}
    #     self.options.add_argument("--disable-bundled-ppapi-flash")  #禁止加载FLSH
    #     self.options.add_argument("--disable-internal-flash")  #禁止加载FLSH
    #     self.options.add_argument("--disable-flash-core-animation")  #

    #     #self.options.add_argument("--disable-popup-blocking")#禁用阻止弹出窗口
    #     #print cur_file_dir()+"\\Chrome\\user_data\\"
    #     #self.options.add_argument("user-data-dir=%s"%(cur_file_dir()+"\\Chrome\\user_data")) #用户配置信息
    #     #self.options.add_argument("disk-cache-dir=%s"%(cur_file_dir()+"\\Chrome\\user_tmp")) #指定缓存Cache路径
    #     #self.options.add_argument("--first run")  #重置到初始状态
    #     self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")

    # # def move_to_element(self,fx,name,x,y):
    # #     blank=self.browser.find_element(fx,".//*[@id='nc_1_clickCaptcha']/div[2]")
    # #     action = ActionChains(self.browser)
    # #     action.move_to_element(blank).perform()  # 移动到write，显示“Mouse moved”
    # #     action.move_by_offset(10, 50).perform()
    # #     action.click()
    # #     # action.move_to_element_with_offset(blank,x,y).perform()
    # #     # action.click_and_hold(blank).perform()  # 2.效果与上句相同，也能起到移动效果


    def web_hd(self):   #网站滑动
        #找到滑动的圆球
        element=self.browser.find_element_by_xpath('.//*[@id="nc_1_n1z"]')
        location=element.location
        #获得滑动圆球的高度
        y=location["y"]
        #鼠标点击元素并按住不放
        #print u"第一步,点击元素"
        ActionChains(self.browser).click_and_hold(on_element=element).perform()
        time.sleep(0.25)
        #print u"第二步，拖动元素"
        ActionChains(self.browser).move_to_element_with_offset(to_element=element, xoffset=400, yoffset= y-400).perform()
        #释放鼠标
        ActionChains(self.browser).release(on_element=element).perform()



    # def open_ie(self):  #打开浏览器
    #     try:
    #         self.browser.close()
    #     except Exception,ex:
    #         pass
    #     try:
    #         #web_close()  #结束浏览器
    #         self.browser = webdriver.Chrome(self.executable_path,chrome_options=self.options)
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:open_ie err:%s==="%(str(ex))
    #         return 1,"api:open_ie err"

    # def close_ie(self):  #关闭浏览器
    #     try:
    #         #self.browser.close()
    #         web_close()  #结束浏览器
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:close_ie err:%s==="%(str(ex))
    #         return 1,"api:close_ie err"

    # def get(self,url):  #打开网页
    #     try:
    #         self.browser.get(url)
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:get err:%s==="%(str(ex))
    #         return 1,"api:get err"

    def stop_sleep(self,sleep):  #隐性延时 等待
        try:
            self.browser.implicitly_wait(string.atoi(sleep)) #隐性等待，最长等30秒
            return 0,None
        except Exception,ex:
            try:
                self.browser.implicitly_wait(2) #隐性等待，最长等30秒
                return 0,None
            except Exception,ex:
                if debug:
                    print "===api:get err:%s==="%(str(ex))
                return 1,"api:stop_sleep err"

    def web_tab_close(self):  #只保存一个标签页
        try:
            all_handles=self.browser.window_handles
            if len(all_handles)>1:
                list_int= len(all_handles)
                for i in range(0, len(all_handles)):
                    #print i, all_handles[i]
                    if i+1>=list_int:
                        self.browser.switch_to_window(all_handles[i])
                        #print "xxxxx",i, all_handles[i]
                        continue   #跳过
                    try:
                        self.browser.switch_to_window(all_handles[i])
                        time.sleep(1)
                        self.browser.close() #关闭当前窗口
                    except Exception,ex:
                        pass
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:web_tab_close err:%s==="%(str(ex))
            return 1,"api:web_tab_close err"
    #==================================================

    def get_url(self):  #获取当前URL
        try:
            D_url=self.browser.current_url
            D_url = uncrypt_decrypt.uncrypt(u"%s"%(D_url))
            return 0,D_url
        except Exception,ex:
            if debug:
                print "===api:get_url err:%s==="%(str(ex))
            return 1,"api:get_url err"

    #def abc_123(self):

    #===============================================
    #操作
    def switch_to_frame(self,fx,name,id):  #iframe的定位
        try:
            if id=="":
                self.browser.switch_to.frame(self.browser.find_element(fx,name))
            else:
                self.browser.switch_to.frame(self.browser.find_elements(fx,name)[int(id)])
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:switch_to_frame err:%s==="%(str(ex))
            return 1,"api:switch_to_frame err"

    def switch_to_default_content(self):  #中切回主文档
        try:
            self.browser.switch_to_default_content()
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:switch_to_default_content err:%s==="%(str(ex))
            return 1,"api:switch_to_default_content err"

    # def send_keys(self,fx,name,key,id):  #发送操作
    #     try:
    #         if id=="":
    #             self.browser.find_element(fx,name).send_keys(key)
    #         else:
    #             self.browser.find_elements(fx,name)[int(id)].send_keys(key)
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:send_keys err:%s==="%(str(ex))
    #         return 1,"api:send_keys err"

    # def click(self,fx,name,id):  #点击操作
    #     try:
    #         if id=="":
    #             self.browser.find_element(fx,name).click()
    #         else:
    #             self.browser.find_elements(fx,name)[int(id)].click()
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:click err:%s==="%(str(ex))
    #         return 1,"api:click err"

    # def clear(self,fx,name,id):  #清空文本
    #     try:
    #         if id=="":
    #             self.browser.find_element(fx,name).clear()
    #         else:
    #             self.browser.find_elements(fx,name)[int(id)].clear()
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:clear err:%s==="%(str(ex))
    #         return 1,"api:clear err"

    # def submit(self,fx,name,id):  #提交表单
    #     try:
    #         if id=="":
    #             self.browser.find_element(fx,name).submit()
    #         else:
    #             self.browser.find_elements(fx,name)[int(id)].submit()
    #         return 0,None
    #     except Exception,ex:
    #         if debug:
    #             print "===api:submit err:%s==="%(str(ex))
    #         return 1,"api:submit err"

    # def size(self,fx,name,id):  #文件大小
    #     try:
    #         if id=="":
    #             size=self.browser.find_element(fx,name).size()
    #         else:
    #             size=self.browser.find_elements(fx,name)[int(id)].size()
    #         return 0,uncrypt_decrypt.uncrypt(u"%s"%(size))
    #     except Exception,ex:
    #         if debug:
    #             print "===api:size err:%s==="%(str(ex))
    #         return 1,"api:size err"

    # def text(self,fx,name,id):  #内容
    #     try:
    #         if id=="":
    #             textx=self.browser.find_element(fx,name).text
    #         else:
    #             textx=self.browser.find_elements(fx,name)[int(id)].text
    #         return 0,uncrypt_decrypt.uncrypt(u"%s"%(textx))
    #     except Exception,ex:
    #         if debug:
    #             print "===api:text err:%s==="%(str(ex))
    #         return 1,"api:text err"

    # def max_window(self):  # 最大化浏览器
    #     try:
    #         self.browser.maximize_window()
    #         return 0, None
    #     except Exception, ex:
    #         if debug:
    #             print "===api:max_window error:%s===" % (str(ex))
    #         return 1, "api:max_window error"

    def set_window_size(self, width, height):  # 设置浏览器宽和高
        try:
            self.browser.set_window_size(int(width), int(height))
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:set_window_size error:%s===" % (str(ex))
            return 1, "api:set_window_size error"

    # def page_forward(self):  # 浏览器页面前进
    #     try:
    #         self.browser.forward()
    #         return 0, None
    #     except Exception, ex:
    #         if debug:
    #             print "===api:page_forward error:%s===" % (str(ex))
    #         return 1, "api:page_forward error"

    # def page_back(self):  # 浏览器页面后退
    #     try:
    #         self.browser.back()
    #         return 0, None
    #     except Exception, ex:
    #         if debug:
    #             print "===api:page_back error:%s===" % (str(ex))
    #         return 1, "api:page_back error"

    # def page_refresh(self):  # 浏览器页面刷新
    #     try:
    #         self.browser.refresh()
    #         return 0, None
    #     except Exception, ex:
    #         if debug:
    #             print "===api:page_refresh error:%s===" % (str(ex))
    #         return 1, "api:page_refresh error"

    def implicitly_wait(self, times):  # 操作等待
        try:
            self.browser.implicitly_wait(times)
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:implicitly_wait error:%s" % (str(ex))
            return 1, "api:implicitly_wait error"

    # def get_title(self):  # 获取页面标题
    #     try:
    #         D_title = self.browser.title
    #         D_title = uncrypt_decrypt.uncrypt(u"%s"%(D_title))
    #         return 0, D_title
    #     except Exception, ex:
    #         if debug:
    #             print "===api:get_title error:%s" % (str(ex))
    #         return 1, "api:get_title error"

    # def current_window_handle(self):  # 获取当前窗口句柄
    #     try:
    #         Current_windowHandle = self.browser.current_window_handle
    #         return 0, Current_windowHandle
    #     except Exception, ex:
    #         if debug:
    #             print "===api: get current handle error:%s===" % (str(ex))
    #         return 1, str(ex)

    # def window_handles(self):  # 获取所有句柄
    #     try:
    #         WindowHandles = self.browser.window_handles
    #         return 0, WindowHandles
    #     except Exception, ex:
    #         if debug:
    #             print "===api: get window handles error:%s===" % (str(ex))
    #         return 1, str(ex)

    def switch_to_alert(self):  # 警告窗口处理
        try:
            Alert = self.browser.switch_to.alert()
            return 0, Alert
        except Exception, ex:
            if debug:
                print "===api:switch_to_alert error:%s===" % (str(ex))
            return 1, "api:switch_to_alert error"

    # def get_cookies(self):  # 获取cookies
    #     try:
    #         cookies = self.browser.get_cookies()
    #         return 0, cookies
    #     except Exception, ex:
    #         if debug:
    #             print "===api:get_cookies error: %s" % (str(ex))
    #         return 1, "api:get_cookies error"
    #==================================================
    def add_cookie(self,name,value,host):  #设置cookie
        try:
            #self.browser.add_cookie({'name': 'SUB', 'value': '_2A253BXZCDeRhGeNG6loY8C_MyTSIHXVUc-CKrDV8PUNbmtAKLUbHkW8DWT7Plq2EVSwQNkHD_r_hKJxhAA..'})
            self.browser.add_cookie({'name': name, 'value': value,'domain':host})
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:add_cookie error:%s" % (str(ex))
            return 1, "api:add_cookie error"

    def delete_all_cookies(self):    # 删除所有cookie
        try:
            self.browser.delete_all_cookies()  # 删除所有cookie
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:delete_all_cookies error:%s" % (str(ex))
            return 1, "api:delete_all_cookies error"
    #==================================================
    # def get_chrome_proxy_extension(self,ff,proxy):
    #     # Chrome代理模板插件(https://github.com/RobinDev/Selenium-Chrome-HTTP-Private-Proxy)目录
    #     CHROME_PROXY_HELPER_DIR = 'Chrome-proxy-helper'
    #     # 存储自定义Chrome代理扩展文件的目录
    #     CUSTOM_CHROME_PROXY_EXTENSIONS_DIR = 'chrome-proxy-extensions'
    #     m = re.compile('([^:]+):([^\@]+)\@([\d\.]+):(\d+)').search(proxy)
    #     if m:
    #         # 提取代理的各项参数
    #         username = m.groups()[0]
    #         password = m.groups()[1]
    #         ip = m.groups()[2]
    #         port = m.groups()[3]
    #         # 创建一个定制Chrome代理扩展(zip文件)
    #         if not os.path.exists(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR):
    #             os.mkdir(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR)
    #         extension_file_path = os.path.join(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR, '{}.zip'.format(proxy.replace(':', '_')))
    #         if not os.path.exists(extension_file_path):
    #             # 扩展文件不存在，创建
    #             zf = zipfile.ZipFile(extension_file_path, mode='w')
    #             zf.write(os.path.join(CHROME_PROXY_HELPER_DIR, 'manifest.json'), 'manifest.json')
    #             # 替换模板中的代理参数
    #             background_content = open(os.path.join(CHROME_PROXY_HELPER_DIR, 'background.js')).read()
    #             #background_content = background_content.replace('%proxy_scheme', "socks5")
    #             #if ff=="https":
    #             #    background_content = background_content.replace('%proxy_scheme', "https")
    #
    #             background_content = background_content.replace('%proxy_host', ip)
    #             background_content = background_content.replace('%proxy_port', port)
    #             background_content = background_content.replace('%username', username)
    #             background_content = background_content.replace('%password', password)
    #             zf.writestr('background.js', background_content)
    #             zf.close()
    #         return extension_file_path
    #     else:
    #         raise Exception('Invalid proxy format. Should be username:password@ip:port')

    def create_proxyauth_extension(self,ff,proxy):
        m = re.compile('([^:]+):([^\@]+)\@([\d\.]+):(\d+)').search(proxy)
        if m:
            # 提取代理的各项参数
            proxy_username = m.groups()[0]
            proxy_password = m.groups()[1]
            proxy_ip = m.groups()[2]
            proxy_port = m.groups()[3]
            plugin_path = cur_file_dir()+"\Chrome\\vimm_chrome_proxyauth_plugin.zip"
            manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy",
                    "tabs",
                    "unlimitedStorage",
                    "storage",
                    "<all_urls>",
                    "webRequest",
                    "webRequestBlocking"
                ],
                "background": {
                    "scripts": ["background.js"]
                },
                "minimum_chrome_version":"22.0.0"
            }
            """
            background_js = string.Template(
                """
                var config = {
                        mode: "fixed_servers",
                        rules: {
                          singleProxy: {
                            scheme: "${scheme}",
                            host: "${host}",
                            port: parseInt(${port})
                          },
                          bypassList: ["foobar.com"]
                        }
                      };
                chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
                function callbackFn(details) {
                    return {
                        authCredentials: {
                            username: "${username}",
                            password: "${password}"
                        }
                    };
                }
                chrome.webRequest.onAuthRequired.addListener(
                            callbackFn,
                            {urls: ["<all_urls>"]},
                            ['blocking']
                );
                """
            ).substitute(
                host=proxy_ip,
                port=proxy_port,
                username=proxy_username,
                password=proxy_password,
                scheme=ff,
            )
            with zipfile.ZipFile(plugin_path, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            return plugin_path
        else:
            raise Exception('Invalid proxy format. Should be username:password@ip:port')

    def http_proxy(self,ff,ip,user,paswod):    #HTTP 代理设置
        try:
            if (len(user)>=1 or len(paswod)>=1):#加载代理模块
                #self.options.add_extension(self.get_chrome_proxy_extension(ff,proxy="%s:%s@%s"%(user,paswod,ip)))
                self.options.add_argument("--start-maximized")
                self.options.add_extension(self.create_proxyauth_extension(ff,proxy="%s:%s@%s"%(user,paswod,ip)))
            if ff=="http":
                self.options.add_argument("--proxy-server=http://%s"%(ip))
            if ff=="https":
                self.options.add_argument("--proxy-server=https://%s"%(ip))
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:http_proxy error:%s" % (str(ex))
            return 1, "api:http_proxy error"
    #==================================================
    def add_argument(self,arg):    #更换头部
        try:
            self.options.add_argument("%s"%(arg))
            return 0, None
        except Exception, ex:
            if debug:
                print "===api:add_argument error:%s" % (str(ex))
            return 1, "api:add_argument error"
    #==================================================
    def div_xy(self,fx,name):   #定位坐标
        try:
            element=self.browser.find_element(fx,name)
            left = element.location_once_scrolled_into_view['x']
            top = element.location_once_scrolled_into_view['y']
            right = element.location_once_scrolled_into_view['x']# +Ax1+ element.size['width']+Ax2
            bottom = element.location_once_scrolled_into_view['y']# +Ay1+element.size['height']+Ay2
            return left,top,right,bottom
        except Exception, ex:
            print "===api:div_xy error:%s" % (str(ex))
            return 0,0,0,0

    def tp_dw(self,fx,name,photo_name,x1,y1,x2,y2,id):  #图片定位
        #print fx,name,photo_name,x1,y1,x2,y2
        try:
            #if not (photo_name in ":\\"):
            #    photo_name="..\\%s"%(photo_name)
            #删除图片
            if os.path.exists(photo_name):
                os.remove(photo_name)
            Ax1=0  #偏移量
            Ay1=0  #偏移量
            Ax2=0  #偏移量
            Ay2=0  #偏移量
            try:
                if x1=="":
                    x1="0"
                if y1=="":
                    y1="0"
                if x2=="":
                    x2="0"
                if y2=="":
                    y2="0"
                Ax1=string.atoi(x1)  #偏移量
                Ay1=string.atoi(y1)  #偏移量
                Ax2=string.atoi(x2)  #偏移量
                Ay2=string.atoi(y2)  #偏移量
            except Exception,ex:
                Ax1=0  #偏移量
                Ay1=0  #偏移量
                Ax2=0  #偏移量
                Ay2=0  #偏移量
            time.sleep(2)
            if id=="":
                element=self.browser.find_element(fx,name)
            else:
                element=self.browser.find_elements(fx,name)[int(id)]
            #print(element.location)                # 打印元素坐标
            #print(element.size)                    # 打印元素大小
            # self.browser.get_screenshot_as_file('bdbutton.bmp')
            # self.browser.save_screenshot('zhidao_hd.png')
            left = element.location_once_scrolled_into_view['x']+Ax1
            top = element.location_once_scrolled_into_view['y']+Ay1
            right = element.location_once_scrolled_into_view['x'] +Ax1+ element.size['width']+Ax2
            bottom = element.location_once_scrolled_into_view['y'] +Ay1+element.size['height']+Ay2
            if right<left or bottom<top:
                res_data="api:tp_dw err x2:%d<x1:%d or y1:%d<y2:%d"%(right,left,bottom,top)
                return 1,res_data
            #im = Image.open('bdbutton.png')
            im = Image.open(StringIO(base64.decodestring(self.browser.get_screenshot_as_base64())))
            im = im.crop((left, top, right, bottom))
            #im.save('bdbuttonx.bmp')
            im.save(photo_name)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:tp_dw err:%s==="%(str(ex))
            return 1,"api:tp_dw err"
    #==================================================
    def is_displayed(self,fx,name,id):  #确定定位是否正确
        try:
            if id=="":
                self.browser.find_element(fx,name).is_displayed()
            else:
                self.browser.find_elements(fx,name)[int(id)].is_displayed()
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:is_displayed err:%s==="%(str(ex))
            return 1,"api:is_displayed err"
    #==================================================
    def get_html(self):  #获取整个页面HTML
        try:
            html=self.browser.page_source
            return 0,uncrypt_decrypt.uncrypt(u"%s"%(html))
        except Exception,ex:
            if debug:
                print "===api:html err:%s==="%(str(ex))
            return 1,"api:html err"
    #==================================================
    def select_index(self,fx,name,index,id):  #选择--内容根据编号选择
        try:
            indexa=1  #编号
            try:
                if index=="":
                    index="1"
                indexa=string.atoi(index)  #编号
            except Exception,ex:
                indexa=1  #编号
            if id=="":
                Select(self.browser.find_element(fx,name)).select_by_index(indexa)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).select_by_index(indexa)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:select_index err:%s==="%(str(ex))
            return 1,"api:select_index err"
    #==================================================
    def select_value(self,fx,name,value,id):  #选择--value内容选择
        try:
            if id=="":
                Select(self.browser.find_element(fx,name)).select_by_value(value)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).select_by_value(value)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:select_value err:%s==="%(str(ex))
            return 1,"api:select_value err"
    #==================================================
    def select_text(self,fx,name,text,id):  #选择--text内容选择
        try:
            if id=="":
                Select(self.browser.find_element(fx,name)).select_by_visible_text(text)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).select_by_visible_text(text)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:select_text err:%s==="%(str(ex))
            return 1,"api:select_text err"
    #==================================================
    def deselect_index(self,fx,name,index,id):  #取消选择--内容根据编号选择
        try:
            indexa=1  #编号
            try:
                if index=="":
                    index="1"
                indexa=string.atoi(index)  #编号
            except Exception,ex:
                indexa=1  #编号
            if id=="":
                Select(self.browser.find_element(fx,name)).deselect_by_index(indexa)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).deselect_by_index(indexa)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:deselect_index err:%s==="%(str(ex))
            return 1,"api:deselect_index err"
    #==================================================
    def deselect_value(self,fx,name,value,id):  #取消选择--value内容选择
        try:
            if id=="":
                Select(self.browser.find_element(fx,name)).deselect_by_value(value)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).deselect_by_value(value)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:deselect_value err:%s==="%(str(ex))
            return 1,"api:deselect_value err"
    #==================================================
    def deselect_text(self,fx,name,text,id):  #取消选择--text内容选择
        try:
            if id=="":
                Select(self.browser.find_element(fx,name)).deselect_by_visible_text(text)
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).deselect_by_visible_text(text)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:deselect_text err:%s==="%(str(ex))
            return 1,"api:deselect_text err"
    #==================================================
    def deselect_all(self,fx,name,id):  #取消选择--全部取消
        try:
            if id=="":
                Select(self.browser.find_element(fx,name)).deselect_all()
            else:
                Select(self.browser.find_elements(fx,name)[int(id)]).deselect_all()
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:deselect_all err:%s==="%(str(ex))
            return 1,"api:deselect_all err"
    #==================================================
    def execute_script(self,js_data):  #执行JS代码
        try:
            print self.browser.execute_script(js_data)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:execute_script err:%s==="%(str(ex))
            return 1,"api:execute_script err"
    #==================================================
    def get_name_value(self,fx,name,value_name,id):  #获取元素值
        try:
            if id=="":
                html=self.browser.find_element(fx,name).get_attribute(value_name)
            else:
                html=self.browser.find_elements(fx,name)[int(id)].get_attribute(value_name)
            html=uncrypt_decrypt.uncrypt(u"%s"%(html))
            return 0,html
        except Exception,ex:
            if debug:
                print "===api:get_name_value err:%s==="%(str(ex))
            return 1,"api:get_name_value err"
    #==================================================
    def win_send_key(self,key):   #向系统发送内容
        try:
            SendKeys.SendKeys(key)
            return 0,None
        except Exception,ex:
            if debug:
                print "===api:win_send_key err:%s==="%(str(ex))
            return 1,"api:win_send_key err"
    #==================================================
    #==================================================
    #==================================================
    #==================================================
    # def file_upload(self,fx,name,key):   #上传文件
    #     self.browser.find_element(fx,name).send_keys(key)
        #self.browser.find_element(fx,name).send_keys("C:\\Users\\Administrator\\Desktop\\123.txt")


    #==================================================
    #==================================================
    #==================================================