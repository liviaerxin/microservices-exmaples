# Restful API and GraphQL

## GraphQL

[graphql](https://graphql.org/learn/)

### GraphQL Java Sever

[graphql-java Tutorial - Introduction](https://www.howtographql.com/graphql-java/0-introduction/)

Extracts:
- Schema-driven development
- Contract-first design


[graphql java documentation](https://www.graphql-java.com/documentation/v12/)

Extracts:
- The default data fetcher in graphql-java is `graphql.schema.PropertyDataFetcher` which has both map support and POJO support.
- 






[Getting started with GraphQL Java and Spring Boot](https://www.graphql-java.com/tutorials/getting-started-with-spring-boot/)

Extracts:
- GraphQL is a query language to retrieve data from a server. It is an alternative to REST, SOAP or gRPC in some way.


[Getting Started with GraphQL and Spring Boot](https://www.baeldung.com/spring-graphql)



### Pagnination, Sorting and Filters

1. Pagnination
here are a number of ways we could do pagination:

- We could do something like friends(first:2 offset:2) to ask for the next two in the list.
- We could do something like friends(first:2 after:$friendId), to ask for the next two after the last friend we fetched.
- We could do something like friends(first:2 after:$friendCursor), where we get a cursor from the last item and use that to paginate.

In general, we've found that cursor-based pagination is the most powerful of those designed. 


[Pagination](https://graphql.github.io/learn/pagination/)

[Paginating Real-Time Data with Cursor Based Pagination](https://www.sitepoint.com/paginating-real-time-data-cursor-based-pagination/)

[Evolving API Pagination at Slack](https://slack.engineering/evolving-api-pagination-at-slack-1c1f644f8e12)

[Understanding pagination: REST, GraphQL, and Relay](https://blog.apollographql.com/understanding-pagination-rest-graphql-and-relay-b10f835549e7)

[GraphQL API pagination implementation](https://medium.com/workflowgen/graphql-api-pagination-implementation-88dba6a061af)

[Relay standard support](https://academy.jahia.com/documentation/developer/dx/7.2/headless-development-with-dx/using-graphql-to-perform-queries#relaystandardsupport)

2. Filters

Designing a complex filtering enale client to have full control over its data requirement and do very complicated filtering pattern.


[Graphcool Query API
](https://www.graph.cool/docs/reference/graphql-api/query-api-nia9nushae#filtering-by-field)