import webbrowser
import os
import re

#page content
main_page_content='''
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="Portfolio">
		<meta name="author" content="Sai Bhavani Kumarn">

		<title>Sai Bhavani Kumar : Projects</title>

		<!-- Bootstrap Core CSS -->
		<link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

		<!-- Custom Fonts -->
		<link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
		<link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
		<link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>

		<!-- Plugin CSS -->
		<link href="vendor/magnific-popup/magnific-popup.css" rel="stylesheet">

		<!-- Theme CSS -->
		<link href="css/creative.min.css" rel="stylesheet">

		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
		    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
		    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->

	</head>

	<body  id="page-top">
	
	<nav id="mainNav" class="navbar navbar-default navbar-fixed-top">
		<div class="container-fluid">
			<!-- Brand and toggle get grouped for better mobile display -->
			<div class="navbar-header">
				<a class="navbar-brand page-scroll" href="index.html">Sai Bhavani Kumarn</a>
			</div>

		</div>
		<!-- /.container-fluid -->
	</nav>
	<header>
        <div class="header-content">
            <div class="header-content-inner">
                <h1 id="homeHeading">Projects</h1>
                <hr>
                <a href="#ProjectList" class="btn btn-primary btn-xl page-scroll">Get Me There</a>
            </div>
        </div>
    </header>
    <section class="bg-dark" id="ProjectList">
			<main class="main-content">
				<div class="fullwidth-block download">
					<div class="container">
						<div class="row">
							 {project_tiles}
						</div>
					</div>
				</div>

				
			</main> <!-- .main-content -->

		</div> <!-- #site-content -->
		
	</section>
    <!-- jQuery -->
    <script src="vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src="vendor/scrollreveal/scrollreveal.min.js"></script>
    <script src="vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

    <!-- Theme JavaScript -->
    <script src="js/creative.min.js"></script>
		
	</body>

</html>
'''


#single project entry html template
project_tile_content_1link = '''
<div class="col-md-4">
	<div class="item">
		<h3 class="text-primary">
			<i class="fa {fa_icon}"></i> <i class="fa {fa_icon2}"></i> {project_title} 
		</h3>
		<p class="text-secondary">{info_1}<br/>
			<span>{info_2}<br/></span>
			<a href="{link}"
			 class="btn-primary btn-xs btn-sq">{link_text}</a>
		</p>
	</div>
</div>
'''

project_tile_content_2links = '''
<div class="col-md-4">
	<div class="item">
		<h3 class="text-primary">
			<i class="fa {fa_icon}"></i> <i class="fa {fa_icon2}"></i> {project_title}
		</h3>
		<p class="text-secondary">{info_1}<br/>
			<span>{info_2}<br/></span>
			<a href="{link_1}"
			 class="btn-primary btn-xs btn-sq">{link_1_text}</a>
			<a href="{link_2}"
			 class="btn-default btn-xs btn-sq" target="_blank">{link_2_text}</a>
		</p>
	</div>
</div>
'''

def create_project_tiles_content(projects):
	content=''
	for project in projects:
		if project.is_git==1:
			content += project_tile_content_2links.format(
				fa_icon=project.fa_icon,
				fa_icon2=project.fa_icon2,
				project_title=project.project_title,
				info_1=project.info_1,
				info_2=project.info_2,
				link_1=project.link_1,
				link_2=project.link_2,
				link_1_text="Download "+project.link_1_text,
				link_2_text="View Details(GitHub)"
			)
		else:
			content += project_tile_content_1link.format(
				fa_icon=project.fa_icon,
				fa_icon2=project.fa_icon2,
				project_title=project.project_title,
				info_1=project.info_1,
				info_2=project.info_2,
				link=project.link_1,
				link_text=project.link_1_text
			)
	return content

def make_project_page(projects):
	output_file = open('projects_new.html','w')
	
	rendered_content = main_page_content.format(
		project_tiles=create_project_tiles_content(projects)
	)
	
	output_file.write(rendered_content)
	output_file.close()
	
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://'+url, new=2)
