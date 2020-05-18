{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "froggy-service.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "froggy-service.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Expand the service names of the chart.
*/}}
{{- define "froggy-service.backend" -}}
    {{- printf "%s-backend" (include "froggy-service.name" .) -}}
{{- end -}}

{{- define "froggy-service.frontend" -}}
    {{- printf "%s-frontend" (include "froggy-service.name" .) -}}
{{- end -}}

{{- define "froggy-service.redis" -}}
    {{- printf "%s-redis" (include "froggy-service.name" .) -}}
{{- end -}}

{{- define "froggy-service.frontend.readinessPath" -}}
    {{- template "froggy-service.backend" . }}:{{ .Values.backend.service.targetPort }}{{ .Values.backend.livenessPath }}
{{- end -}}

{{- define "froggy-service.environment" -}}
    {{- printf "%s-env" (include "froggy-service.name" .) -}}
{{- end -}}

{{- define "froggy-service.cloudsqlProxy" -}}
    {{- printf "%s-cloudsql-proxy" (include "froggy-service.name" .) -}}
{{- end -}}

{{- define "froggy-service.ingress" -}}
    {{- printf "%s-ingress" (include "froggy-service.name" .) -}}
{{- end -}}

{{/*
Function to parse .env file and output in yaml
KEY_ENV1=VAL_ENV1      KEY_ENV1: base64(VAL_ENV1)
KEY_ENV2=VAL_ENV2  =>  KEY_ENV2: base64(VAL_ENV2)
KEY_ENV3=VAL_ENV3      KEY_ENV3: base64(VAL_ENV3)
Usage:
{{ tuple . "configs/backend/php-fpm/.env" | include "env.parseFile" | indent 2}}
*/}}
{{- define "env.parseFile" -}}
{{- $scope := index . 0 -}}
{{- $filePath := index . 1 -}}
{{- range $scope.Files.Lines $filePath -}}
{{- $a := splitn "=" 2 . -}}
{{- if $a._0 -}}
{{ $a._0 }}: {{ $a._1 | b64enc }}
{{ end -}}
{{- end -}}
{{- end -}}
