$(document).ready(function() {
    doWork();
});

function doWork() {
    d3.json("samples.json").then((data) => {
        console.log(data);

        // populate the dropdown
        data.names.forEach(function(val) {
            var newOption = `<option>${val}</option>`;
            $('#selDataset').append(newOption);
        });

        // grab first name in dropdown

        // filter the metadata

        // build that div

    });
}