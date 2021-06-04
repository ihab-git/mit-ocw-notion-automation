import requests
from bs4 import BeautifulSoup
import os


def get_video_lecture_from_lecture_site_link(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for script in soup.find_all("script"):
        for content in script.contents:
            split = content.split("\'")
            if len(split) > 3:
                if "https://www.youtube.com" in split[3]:
                    return split[3]
    return "NONE FOUND"


def get_lecture_data(path):
    data = {}

    # LECTURE NAME
    with open(path+r"/index.htm.xml") as f:
        xml_content = f.read()
    xml = BeautifulSoup(xml_content, "html.parser")
    data["name"] = xml.find("lom:string").contents[0]

    # LECTURE VIDEO LINK
    lecture_url = "https://ocw.mit.edu" + xml.find("lom:location").contents[0]
    data["video"] = get_video_lecture_from_lecture_site_link(lecture_url)

    return data


def get_all_lecture_paths(path):
    return [path+"\\"+i for i in os.listdir(path) if i.startswith("lecture-")]


def get_course_data(path):
    data = {}
    with open(path+r"/index.htm.xml") as f:
        xml_content = f.read()
    xml = BeautifulSoup(xml_content, "html.parser")
    data["name"] = xml.find("lom:string").contents[0]
    data["summary"] = xml.find("lom:description").contents[1].text
    data["url"] = "https://ocw.mit.edu" + xml.find("lom:location").contents[0]
    data["course_number"] = xml.find("lom:entry").contents[0]
    instructors = []
    for contribute in xml.find_all("lom:contribute"):
        instructors.append(contribute.find("lom:entity").contents[0])
    data["instructors"] = instructors
    return data
