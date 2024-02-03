// --------------------- charts ------------------------------

//---------------------------- bar chart ------------------
var options = {
    series: [{
    data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
  }],
    chart: {
    type: 'bar',
    height: 350
  },
  plotOptions: {
    bar: {
      borderRadius: 4,
      horizontal: true,
    }
  },
  dataLabels: {
    enabled: false
  },
  xaxis: {
    categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan',
      'United States', 'China', 'Germany'
    ],
  }
  };

  var chart = new ApexCharts(document.querySelector("#bar-chart"), options);
  chart.render();


//   -------------------- chart ---------------------



// var options = {
//     series: [{
//     name: 'PRODUCT A',
//     data: [44, 55, 41, 67, 22, 43]
//   }, {
//     name: 'PRODUCT B',
//     data: [13, 23, 20, 8, 13, 27]
//   }, {
//     name: 'PRODUCT C',
//     data: [11, 17, 15, 15, 21, 14]
//   }, {
//     name: 'PRODUCT D',
//     data: [21, 7, 25, 13, 22, 8]
//   }],
//     chart: {
//     type: 'bar',
//     height: 350,
//     stacked: true,
//     toolbar: {
//       show: true
//     },
//     zoom: {
//       enabled: true
//     }
//   },
//   responsive: [{
//     breakpoint: 480,
//     options: {
//       legend: {
//         position: 'bottom',
//         offsetX: -10,
//         offsetY: 0
//       }
//     }
//   }],
//   plotOptions: {
//     bar: {
//       horizontal: false,
//       borderRadius: 10,
//       dataLabels: {
//         total: {
//           enabled: true,
//           style: {
//             fontSize: '13px',
//             fontWeight: 900
//           }
//         }
//       }
//     },
//   },
//   xaxis: {
//     type: 'datetime',
//     categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
//       '01/05/2011 GMT', '01/06/2011 GMT'
//     ],
//   },
//   legend: {
//     position: 'right',
//     offsetY: 40
//   },
//   fill: {
//     opacity: 1
//   }
//   };

//   var chart = new ApexCharts(document.querySelector("#area-chart"), options);
//   chart.render();

// var sectionData = category_data.section_article_counts;
// var sentimentData = category_data.sentiment_counts_by_section;
// console.log(sectionData)

// Créez des tableaux pour stocker les données
// var sections = [];
// var counts = [];
// var positif = [];
// var negatif = [];
// var neutre = [];

// // Parcourez les données et remplissez les tableaux
// for (var section in sectionData) {
//     sections.push(section);
//     counts.push(sectionData[section]);
//     positif.push(sentimentData[section]['positif']);
//     negatif.push(sentimentData[section]['négatif']);
//     neutre.push(sentimentData[section]['neutre']);
// }


// var ctx = document.getElementById('myChart').getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: sections,
//         datasets: [
//             {
//                 label: 'Count',
//                 data: counts,
//                 backgroundColor: 'blue',
//             },
//             {
//                 label: 'Positif',
//                 data: positif,
//                 backgroundColor: 'green',
//             },
//             {
//                 label: 'Negatif',
//                 data: negatif,
//                 backgroundColor: 'red',
//             },
//             {
//                 label: 'Neutre',
//                 data: neutre,
//                 backgroundColor: 'gray',
//             },
//         ],
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true,
//             },
//         },
//     },
// });

