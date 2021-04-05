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
      url: 'http://127.0.0.1:8000/',
      propertyTypesList : [],
      messageCreateTransaction: '',
      messageTransaction: '',
      messageCreateProperty: '',
      messageProperty: ''
  },
  mounted: function(){
    this.onloadReviews();
    this.onloadTransactions();
    this.onloadStates();
    this.onloadProperties();
    this.onloadPropertyTypes();
    this.getTransaction();
    this.postTransactions();
    this.deleteTransaction();
    this.putTransaction();
    this.onloadCities();
    this.onloadCategories();
    this.postProperties();
    this.getProperty();
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
          var $selectTransactionsCreate = $('#propertyTypesTransactionCreate');
          var $selectPropertyTypes = $('#propertyTypesTransaction');

          $("#slectTransactions").empty();
          $("#propertyTypesTransactionCreate").empty();
          $("#propertyTypesTransaction").empty();

          this.onloadPropertyTypes();
          $.each(data, function(id, slug){
            $selectTransactions.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
          });

          $.each(this.propertyTypes, function(id, slug){
            $selectTransactionsCreate.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
            $selectPropertyTypes.append(
              '<option id = "propertyType' + slug.id +'"  value=' + slug.id + '>' + slug.slug + '</option>'
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
          document.getElementById("slugTransaction").value = data["slug"];

          var $selectPropertyTypes = $('#propertyTypesTransaction');
          $.each(data["propertyTypes"], function(id, slug){
              //document.getElementById("propertyType"+slug.id).selected = true;
          });
      });
    },

    postTransactions: function () {
      var slug = document.getElementById("slugTransactionCreate").value;
      var propertyTypes = $('#propertyTypesTransactionCreate').val();
      var propertyTypesInt = []

      for (propertyType in propertyTypes){
        propertyTypesInt.push(parseInt(propertyTypes[propertyType]));
      }

      var urltransactions = this.url + 'transactions/';
      var data = {
        slug: slug,
        propertyTypes: propertyTypesInt
      }

      fetch(urltransactions, {
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(data => {
          this.messageCreateTransaction = data.message;
          this.onloadTransactions();
        });

    },

    deleteTransaction: function(){
      var id = document.getElementById("slectTransactions").value;
      var urltransactions = this.url + 'transactions/' + id;

      fetch(urltransactions,{
        method: 'DELETE',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data=>{
        this.messageTransaction = data.message;
        this.onloadTransactions();
      })
    },

    putTransaction: function(){
      var id = document.getElementById("slectTransactions").value;
      var urltransactions = this.url + 'transactions/' + id;

      var slug = document.getElementById("slugTransaction").value;
      var propertyTypes = $('#propertyTypesTransaction').val();
      var propertyTypesInt = []

      for (propertyType in propertyTypes){
        propertyTypesInt.push(parseInt(propertyTypes[propertyType]));
      }

      fetch(urltransactions,{
        method: 'DELETE',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data=>{
        this.messageTransaction = data.message;
        this.onloadTransactions();
      })
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
          this.onloadCities();
          this.onloadCategories();
          var $selectCity = $('#cityPropertyCreate');
          var $selectCategory = $('#categoryPropertyCreate');
          var $selectCityp = $('#cityProperty');
          var $selectCategoryp = $('#categoryProperty');
          var $slectProperty = $('#slectProperty');

          $("#cityPropertyCreate").empty();
          $("#categoryPropertyCreate").empty();
          $('#cityProperty').empty();
          $('#categoryProperty').empty();

          $.each(data, function(id, slug){
            $slectProperty.append(
              '<option value=' + slug.id + '>' + slug.title + '</option>'
            );
          });

          $.each(this.cities, function(id, slug){
            $selectCity.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
            $selectCityp.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
          });

          $.each(this.properties, function(id, slug){
            $selectCategory.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
            $selectCategoryp.append(
              '<option value=' + slug.id + '>' + slug.slug + '</option>'
            );
          });
      });
    },

    postProperties: function(){
      var title = document.getElementById("slugTransactionCreate").value;
      var image = document.getElementById("imagePropertyCreate").value;
      var price = document.getElementById("pricePropertyCreate").value;
      var city = $('#cityPropertyCreate').val();
      var baths = document.getElementById("bathsPropertyCreate").value;
      var beds = document.getElementById("bedsPropertyCreate").value;
      var sqrft = document.getElementById("sqftPropertyCreate").value;
      var category = $('#categoryPropertyCreate').val();
      var categoryInt = [];

      var city_int = parseInt(city);

      for (cat in category){
        categoryInt.push(parseInt(category[cat]));
      };
      var urlproperties = this.url + 'properties/';
      var data = {
        title: title,
        image: propertyTypesInt,
        price: price,
        city: city_int,
        baths: baths,
        beds: beds,
        sqrft: sqrft,
        category: categoryInt
      }

      fetch(urlproperties, {
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(data => {
          this.messageCreateProperty = data.message;
          this.onloadTransactions();
        });
    },

    getProperty: function (){
      var id = document.getElementById("slectProperty").value;
      var urlproperties = this.url + 'properties/' + id;
      fetch(urlproperties,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data => {
        var title = document.getElementById("slugTransactionCreate").value = data['title'];
        var image = document.getElementById("imagePropertyCreate").value= data['image'];
        var price = document.getElementById("pricePropertyCreate").value= data['price'];
        var baths = document.getElementById("bathsPropertyCreate").value= data['baths'];
        var beds = document.getElementById("bedsPropertyCreate").value= data['beds'];
        var sqrft = document.getElementById("sqftPropertyCreate").value= data['sqrft'];
      });
    },

    deleteProperty: function(){
      var id = document.getElementById("slectProperty").value;
      var urlproperties = this.url + 'properties/' + id;
      fetch(urlproperties,{
        method: 'DELETE',
        headers:{
            'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(data=>{
        this.messageProperty = data.message;
        this.onloadProperties();
      })
    }
  }
});
