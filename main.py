from mit_site import *
import csv

MAIN_PATH = r"C:\Users\ihab1\Desktop\6-034-fall-2010\6-034-fall-2010\contents"


def main():
    with open("output/out.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Lec Number", "Name", "Video Link", "Completed"])
        for lecture in get_all_lecture_paths(MAIN_PATH + "\lecture-videos"):
            data = get_lecture_data(lecture)
            lecture_num = data["name"].split(" ")[1].replace(":", "")
            writer.writerow([lecture_num, data["name"], data["video"], "No"])
    c_data = get_course_data(MAIN_PATH)

    print(
        f"""
        NAME-{c_data["name"]}
        
        SUMMARY-{c_data["summary"]}
        
        URL-{c_data["url"]}
        
        COURSE NUMBER-{c_data["course_number"]}
        
        INSTRUCTORS-{" ".join(c_data["instructors"])}
        """
    )


if __name__ == "__main__":
    main()
