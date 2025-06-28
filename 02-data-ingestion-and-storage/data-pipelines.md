# Amazon Data Pipeline (Legacy)

AWS Data Pipeline is now in maintenance mode (no longer available to new customers), but existing customers can continue using it. It provides a way to reliably process and move data between different AWS compute and storage services and on-premises data sources.

Key components include:

- **Pipeline Definition**: Specifies the business logic of your data management
- **Pipeline**: Schedules and runs tasks by creating Amazon EC2 instances to perform defined work activities
- **Task Runner**: Polls for tasks and then performs those tasks (e.g., copying log files to Amazon S3)

## AWS Glue vs. AWS Data Pipeline Comparison

| Feature                      | AWS Data Pipeline                                     | AWS Glue                                          |
| ---------------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| **Service Type**             | Managed workflow service                              | Managed ETL service                               |
| **Serverless**               | No - launches compute resources in your account       | Yes - fully serverless                            |
| **Underlying Technology**    | Custom workflows using EC2/EMR                        | Apache Spark-based                                |
| **Programming Model**        | JSON pipeline definitions                             | Python or Scala scripts                           |
| **User Interface**           | Drag-and-drop; Web console; CLI                       | Visual and code-based                             |
| **Data Processing**          | Batch only                                            | Batch and streaming                               |
| **Scalability**              | Scales up to 10^6 files                               | Scales on demand                                  |
| **Data Discovery**           | Limited                                               | Data Catalog and Crawlers                         |
| **Built-in Transformations** | Limited                                               | 16+ built-in transformations; 250+ in DataBrew    |
| **Orchestration**            | Yes - scheduling, dependency tracking, error handling | Yes - triggers, workflows, blueprints             |
| **Pricing Model**            | Based on activity frequency and execution location    | Hourly rate billed by the second                  |
| **Data Sources**             | S3, RDS, DynamoDB, Redshift, on-premises              | 80+ data sources including JDBC, NoSQL, streaming |
| **Visual Data Prep**         | No                                                    | Yes, via DataBrew                                 |
| **CDC Support**              | No                                                    | Yes, via Elastic Views                            |
| **Complex Transformation**   | Up to 100 objects per pipeline                        | Integration with Step Functions                   |
| **Best For**                 | Simple data movement between AWS services             | Complex ETL with Spark, data discovery, data prep |

## Additional Resources

- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [AWS Solutions for Data Pipelines](https://aws.amazon.com/solutions/implementations/aws-data-lake-solution/)
- [AWS Database Migration Service](https://aws.amazon.com/dms/)
- [Amazon MSK Documentation](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [AWS Step Functions for Data Processing](https://docs.aws.amazon.com/step-functions/latest/dg/use-cases-data-processing.html)
