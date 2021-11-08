FROM alpine:3.10
LABEL "repository"="https://github.com/praveenb1988/labeler-commit"
LABEL "homepage"="https://github.com/praveenb1988/labeler-commit"
LABEL "maintainer"="Praveenb1988"

COPY entrypoint.sh /entrypoint.sh

RUN apk update && apk add bash git curl jq && apk add --update nodejs npm && npm install -g semver

ENTRYPOINT ["/entrypoint.sh"]
