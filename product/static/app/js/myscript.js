$(document).ready(function () {
    // Plus icon click event
    $('.plus_cart').click(function () {
        var id = $(this).attr("pid").toString();
        var quantityElem = $(this).siblings(".quantity");
        $.ajax({
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log('data = ', data);
                quantityElem.text(data.quantity);
                $("#amount").text(data.amount);
                $("#totalamount").text(data.totalamount);
            }
        });
    });

    // Minus icon click event
    $('.minus_cart').click(function () {
        var id = $(this).attr("pid").toString();
        var quantityElem = $(this).siblings(".quantity");
        $.ajax({
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log('data = ', data);
                quantityElem.text(data.quantity);
                $("#amount").text(data.amount);
                $("#totalamount").text(data.totalamount);
            }
        });
    });

    // Remove icon click event
    $('.remove_cart').click(function () {
        var id = $(this).attr("pid").toString();
        var rowToRemove = $(this).closest('.cart-item-row');
        $.ajax({
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function (data) {
                $("#amount").text(data.amount);
                $("#totalamount").text(data.totalamount);
                rowToRemove.remove();
            }
        });
    });

    // Plus Wishlist
    $('.plus-wishlist').click(function () {
        var id = $(this).attr("pid").toString();
        $.ajax({
            type: "GET",
            url: "/pluswishlist",
            data: {
                prod_id: id
            },
            success: function (data) {
                window.location.href = `http://localhost:8000/product-detail/${id}`;
            }
        });
    });

    // Minus Wishlist
    $('.minus-wishlist').click(function () {
        var id = $(this).attr("pid").toString();
        $.ajax({
            type: "GET",
            url: "/minuswishlist",
            data: {
                prod_id: id
            },
            success: function (data) {
                window.location.href = `http://localhost:8000/product-detail/${id}`;
            }
        });
    });
});
