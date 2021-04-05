var app = new Vue ({
  el: '#app',
  data: {
      reviews: '',
      reviewsStatus:  '',
      transactions: '',
      transactionsStatus: '',
      propertyTypes: '',
      propertyTypesStatus: '',
      states: '',
      statesStatus: '',
      cities: '',
      citiesStatus: '',
      categories: '',
      categoriesStatus: '',
      properties: '',
      propertiesStatus: '',
      url: 'http://127.0.0.1:8000/'
  },
  mounted: function(){
    this.onloadReviews();
    this.onloadTransactions();
    this.onloadPropertyTypes();
    this.onloadStates();
    this.onloadCities();
    this.onloadCategories();
    this.onloadProperties();
  },
  methods: {
    onloadReviews: function () {
      var urlreview = this.url + 'reviews/';
      fetch(urlreview,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(function(response){
        console.log (response.status);
        this.reviewsStatus = response.status;
        return response.json();
      })
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.reviews = data;
      });
    },

    idReviews: function (method, id){
      var url = this.url + 'reviews/' + id;
      fetch(url, {

      });
    },

    onloadTransactions: function (){
      var urltransactions = this.url + 'transactions/';
      fetch(urltransactions,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.transactions = data;
          var $selectTransactions = $('#slectTransactions');

          $.each(data, function(id, slug){
            $selectTransactions.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
          });
      });
    },

    getTransaction: function (){
      var id = document.getElementById("slectTransactions").value;
      var urltransactions = this.url + 'transactions/' + id;
      fetch(urltransactions,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
        console.log(data);
          document.getElementById("slugTransaction").value = data["slug"];

          var $selectPropertyTypes = $('#propertyTypesTransaction');
          $.each(data["propertyTypes"], function(id, slug){
            $selectPropertyTypes.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
          });
      });
    },

    postTransactions: function () {

    },

    onloadPropertyTypes: function (){
      var urlpropertyTypes = this.url + 'propertyTypes/';

      fetch(urlpropertyTypes,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.propertyTypes = data;
      });
    },

    onloadStates: function (){
      var urlstates = this.url + 'states/';

      fetch(urlstates,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.states = data;
      });
    },

    onloadCities: function (){
      var urlcities = this.url + 'cities/';

      fetch(urlcities,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.cities = data;
      });
    },

    onloadCategories: function (){
      var urlcategories = this.url + 'categories/';

      fetch(urlcategories,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.categories = data;
      });
    },

    onloadProperties: function (){
      var urlproperties = this.url + 'properties/';

      fetch(urlproperties,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
          this.properties = data;
      });
    },
  }
});
