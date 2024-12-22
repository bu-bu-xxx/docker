FROM golang:latest

WORKDIR /usr/src/app

COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . .
RUN go build

CMD [ "sh", "-c", "./chaturbate-dvr --gui-username ${GUI_USERNAME} --gui-password ${GUI_PASSWORD} --filename-pattern ${FILENAME_PATTERN} --port ${PORT}" ]
