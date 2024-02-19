"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    nested_dict = {}
    csvfile = open(filename, 'r', newline='', encoding='utf-8')
    csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
    for row in csvreader:
        key = row[keyfield]
        del row[keyfield]
        nested_dict[key] = row

    return nested_dict


def build_plot_values(gdpinfo, gdpdata):
    min_year = gdpinfo['min_year']
    max_year = gdpinfo['max_year']
    
    plot_values = []
    
    for year in range(min_year, max_year + 1):
        if str(year) in gdpdata:
            plot_values.append((year, float(gdpdata[str(year)])))
    
    return plot_values


def build_plot_dict(gdpinfo, country_list):
    plot_dict = {}
    gdpdata = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"]
                                      , gdpinfo["separator"], gdpinfo["quote"])
    for country in country_list:
        # print(country)
        if country in gdpdata:
            # print(11)
            plot_values = build_plot_values(gdpinfo, gdpdata[country])
            plot_dict[country] = plot_values
        else:
            plot_dict[country] = []
    
    return plot_dict


def render_xy_plot(gdpinfo, country_list, plot_file):
    plot_dict = build_plot_dict(gdpinfo, country_list)
    
    xy_chart = pygal.XY(title='GDP Data', x_title='Year', y_title='GDP')
    
    for country, plot_values in plot_dict.items():
        xy_chart.add(country, plot_values)
    
    xy_chart.render_to_file(plot_file)


def test_render_xy_plot():
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
                   "isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

test_render_xy_plot()