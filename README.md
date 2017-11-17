# Cloudformation templates

This repo contains all the cloudformation templates needed for the
yourdomain.tld.  This will include the Route53 Hosted Zone, Record Sets, S3
buckets, and CloudFront resources needed for each domain.

## Important

Replace all "yourdomain.tld" or "yourdomain-tld" with your custom domain (ie
williamsbdev.com). Also update the default values for the parameters in the
`yourdomain-tld.json` to reflect the values you desire (DomainName, AcmArn,
Region).

## CloudFront IP ranges

This template will get out of date with the CloudFront IP ranges so I have
included a script that will gather the latest CloudFront IP ranges at the time.

### yourdomain-tld stack creation

`aws cloudformation create-stack --stack-name yourdomain-tld --template-body file://yourdomain-tld.json`
