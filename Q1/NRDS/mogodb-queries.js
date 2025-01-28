// Exercises 1 //

{
    _id: 201,
    CustomerID: 501,
    OrderDate: 2023-09-15,
    OrderDetails: [
        {
        ProductID: 1, 
        Quantity: 1,
        ProductName: Laptop,
        Price: 1200
        },
        {
        ProductID: 3, 
        Quantity: 2,
        ProductName: Headphone,
        Price: 150
        }
    ]
}


// Exercises 2 //

db.movies.find({ratings: {$gt: 9.0}})

db.movies.updateMany({director.name: Crisotpher Nolan}, {$set: {age:69}})


// Exercises 3 //

db.employees.find({$or: [{departament:HR},{salary:{$lt: 60000}}]})

db.employees.find({$and: [{age:{$gt:30}},{departament:Engineering}]})


// Exercises 4 //

db.people.find({
"hobbies": {$all: ["Gaming", "Chess"], $ne: "Yoga"}
})



db.restaurants.aggregate([ { $match: { cuisine: "American" } },
                        { $group: { _id: "$borough", count: {$count: {}}}}, 
                        { $sort: {count: 1 }}])

db.collection.createIndex({"address.coord":"2d"})

db.restaurants.aggregate([
    {
        $match: {
            "grades.score": { $gt: 50 }, 
            "address.coord": {
                $geoWithin: {
                    $box: [[-74, 40.5], [-73.5, 40.7]]}
                }
        }
    },
    {   
        $count: "restaurants" 
    }
])

db.restaurants.createIndex({ "address.coord": "2dsphere" })

db.restaurants.find({
    "address.coord": {
        $nearSphere: {
            $geometry: {
                type: "Point",
                coordinates: [-74.0179141, 40.7583243]
            },
            $maxDistance: 1500
        }
    }},
    {name: 1})

                        
