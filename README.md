# Cloudformation templates

This repo contains all the cloudformation templates needed for the
yourdomain.tld.  This will include the Route53 Hosted Zone, Record Sets, S3
buckets, and CloudFront resources needed for each domain.

## Important

Replace all "yourdomain.tld" or "yourdomain-tld" with your custom domain (ie
williamsbdev.com).

### yourdomain-tld stack creation

`aws cloudformation update-stack --stackname yourdomain-tld --template-body file://yourdomain-tld.json`
