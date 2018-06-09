import project
import projectDevelop

projects = []

count = int(raw_input())

for i in xrange(count):
	p = project.Project(int(raw_input()), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input())
	projects.append(p)
	raw_input()

projectDevelop.make_project_page(projects)
