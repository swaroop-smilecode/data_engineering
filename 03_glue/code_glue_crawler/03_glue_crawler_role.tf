# IAM role
resource "aws_iam_role" "glue_crawler_role" {
  name = "glue_crawler_role"

  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "glue.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  })
}

# IAM policy
resource "aws_iam_role_policy" "glue_crawler_policy" {
  name = "glue_crawler_policy"
  role = aws_iam_role.glue_crawler_role.name

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Sid" : "VisualEditor0",
        "Effect" : "Allow",
        "Action" : [
          "s3:*",
          "logs:*",
          "glue:*"
        ],
        "Resource" : "*"
      }
    ]
  })
}
