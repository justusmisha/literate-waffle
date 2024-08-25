class UserEndpoints:
    # Parser endpoints
    save_by_query = '/api/v1/parser/save/by_query'
    link_executor = '/api/v1/parser/execute'
    parse_one_link = '/api/v1/parser/one_link'
    # Google endpoints
    create_sheet = '/api/v1/google/create'
    # Seller endpoints
    add_seller = '/api/v1/seller/add'
    parse_seller = '/api/v1/seller/parse'
    # Fetch endpoints
    all_queries = '/api/v1/fetch/query/all'
    all_sellers = '/api/v1/fetch/seller/all'
    all_google_sheets = '/api/v1/fetch/google/all'
    google_sheet_by_name = '/api/v1/fetch/google/by_name'
    # Delete endpoints
    delete_query = '/api/v1/fetch/query/query_name'
    delete_seller = '/api/v1/fetch/seller/seller_name'

