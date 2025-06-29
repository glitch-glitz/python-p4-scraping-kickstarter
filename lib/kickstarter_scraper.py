from bs4 import BeautifulSoup
import ipdb

# CSS selectors reference:
# projects: kickstarter.select("li.project.grid_4")
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text.strip()

        projects[title] = {
            'image_link': project.select("div.project-thumbnail a img")[0]['src'],
            'description': project.select("p.bbcard_blurb")[0].text.strip(),
            'location': project.select("ul.project-meta span.location-name")[0].text.strip(),
            'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "").strip()
        }

    return projects

if __name__ == "__main__":
    project_data = create_project_dict()
    # Uncomment the next line to debug in ipdb
    # ipdb.set_trace()
    print(project_data)
