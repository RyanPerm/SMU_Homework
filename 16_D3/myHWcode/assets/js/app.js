$(document).ready(function() {
    makePlot();
});

function makePlot() {
    d3.csv("data.csv").then(function(data) {
        console.log(data);
        // make the plot
        // STEP 1: set up the chart
        var svgWidth = 960;
        var svgHeight = 500;
        var margin = {
            top: 20,
            right: 40,
            bottom: 60,
            left: 50
        };
        // get the area for the viz itself
        var chart_width = svgWidth - margin.left - margin.right;
        var chart_height = svgHeight - margin.top - margin.bottom;
        // STEP 2: CREATE THE SVG (if it doesn't exist already)
        var svg = d3.select("#scatter")
            .append("svg")
            .attr("width", svgWidth)
            .attr("height", svgHeight);
        var chartGroup = svg.append("g")
            .attr("transform", `translate(${margin.left}, ${margin.top})`);
        // STEP 3: PREPARE THE DATA
        var timeParser = d3.timeParse("%d-%b");
        data.forEach(function(row) {
            row.date = timeParser(row.date); //cast the date string to a datetime object data type
        });
        // STEP 4: CREATE SCALES
        var col1_max = d3.max(data, d => d.morning);
        var col2_max = d3.max(data, d => d.evening);
        var total_max = d3.max([col1_max, col2_max]);
        var xScale = d3.scaleTime()
            .domain(d3.extent(data, d => d.date))
            .range([0, chart_width]);
        var yScale = d3.scaleLinear()
            .domain([0, total_max])
            .range([chart_height, 0]);
        // STEP 5: CREATE THE AXES
        var leftAxis = d3.axisLeft(yScale);
        var bottomAxis = d3.axisBottom(xScale).tickFormat(d3.timeFormat("%d-%b")); // cast the datetime back to a string for display (only for time series)
        chartGroup.append("g")
            .attr("transform", `translate(0, ${chart_height})`)
            .call(bottomAxis);
        chartGroup.append("g")
            .call(leftAxis);
        // STEP 6: CREATE THE GRAPH
        // for line graphs - create line generator and then draw the line
        var line_gen1 = d3.line()
            .x(d => xScale(d.date))
            .y(d => yScale(d.morning));
        var line_gen2 = d3.line()
            .x(d => xScale(d.date))
            .y(d => yScale(d.evening));
        chartGroup.append("path")
            .attr("d", line_gen1(data))
            .classed("line green", true);
        chartGroup.append("path")
            .attr("d", line_gen2(data))
            .classed("line orange", true);
    }).catch(function(error) {
        alert("YOU BROKE SOMETHING. JK. It was Aakash.");
        console.log(error);
    });
}