var monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];
var dayNames = ["Sun, ", "Mon, ", "Tue, ", "Wed, ", "Thu, ", "Fri, ", "Sat, "]


var  d = new Date();

  // convert to msec
  // add local time zone offset
  // get UTC time in msec
var  utc = d.getTime() + ((d.getTimezoneOffset()+8*60) * 60000);

  // create new Date object for different city
  // using supplied offset
 // nd = new Date(utc + (3600000*offset));
var newDate = new Date(utc);

$('#Date').html(dayNames[newDate.getDay()] + " " + newDate.getDate() + ' ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());
