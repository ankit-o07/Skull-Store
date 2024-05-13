

$("#commentFrom").submit(function(e){
    e.preventDefault();
    
    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),
        dataType:"json",
        url:$(this).attr("action"),
        success: function(res){
            console.log("comment save to db");

            if(res.bool== true ){
                
            }
        }
    })


})




$(document).ready(function(){
    $(".filter-checkbox, #price-filter-btn").on("click",function(){
        console.log("A checkbox have been clickec")

        let filter_object = {}
        let min_price = $("#max_price").attr('min')
        let max_Price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_Price;
        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            // console.log("Start")
            // console.log("Filter value is:" , filter_value)
            // console.log("Filter key is:" , filter_key)
            // console.log("end")
            
            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key +']:checked')).map(function(element){
                return element.value
            })

        })

        console.log("Filter Object is: ",filter_object);
        $.ajax({
            url: '/filter-product',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Sending Data...");
            },

            success:function(response){
                console.log("Start")
                console.log(response);
                console.log("done ?");
               $("#filtered-product").html(response.data)
            }
        })
    })

   


    
    $('#max_price').on('blur',function(){
        console.log("I am clicked")
        let min_price = $(this).attr("min");
        let max_price = $(this).attr("max");
        let current_price = $(this).val();

        if(current_price < parseInt(min_price) || current_price > parseInt(max_price)){
            min_Price = Math.round(min_price*100)/100
            max_Price = Math.round(max_price*100)/100

            alert("Price  must between " , min_price , " and " ,  max_price)
            $(this).val(min_price)
            $("#range").val(min_price)

            $(this).focus()
            return false
        }


    })


})





// Add to cart functionality


$(".add-to-cart-btn").on("click" , function(){
    let this_val = $(this)
    let index = this_val.attr("data-index")

    


    let quantity = $(".product-quantity-"+ index).val()
    let product_title = $(".product-title-"+ index).val()

    let product_id = $(".product-id-" + index).val() 
    let product_price = $(".current-product-price-"+ index).text()

    let product_pid = $(".product-pid-"+ index).val()
    let product_image = $(".product-image-" + index).val()

    console.log("Quantity:", quantity)
    console.log("Product ID:" , product_id)
    console.log("Title:", product_title)
    console.log("Price:", product_price )
    console.log("Pid" , product_pid)
    console.log("p image" , product_image)
    console.log("index" , index)
    console.log("Current Element" , this_val)
    
    

    $.ajax({
        url: '/add-to-cart',
        data:{
            'id':product_id,
            'pid':product_pid,
            'image': product_image,
            'qty':quantity,
            'title':product_title,
            'price':product_price,
        },
        dataType:'json',
        beforeSend: function(){
            console.log("Adding product to cart....")
        },

        success: function(res){
            this_val.html("✔")
            $(".cart-items.count").text(res.totalcartitem)
        }
    })
})




// $("#add-to-cart-btn").on("click" , function(){
//     let quantity = $("#product-quantity").val()
//     let product_title = $(".product-title").val()
//     let product_id = $(".product-id").val() 
//     let product_price = $(".current-product-price").text()
//     let this_val = $(this)

//     console.log("Quantity:", quantity)
//     console.log("Product ID:" , product_id)
//     console.log("Title:", product_title)
//     console.log("Price:", product_price )
//     console.log("This:" , this_val)

//     $.ajax({
//         url: '/add-to-cart',
//         data:{
//             'id':product_id,
//             'qty':quantity,
//             'title':product_title,
//             'price':product_price,
//         },
//         dataType:'json',
//         beforeSend: function(){
//             console.log("Adding product to cart....")
//         },

//         success: function(res){
//             this_val.html("Item added to cart")
//             console.log("Added product to cart!")
//             $(".cart-items.count").text(respones.total)
//         }
//     })
// })