# Security Policy

This document outlines the security policy for the "video_div" (Video Splitter / 동영상 분할 프로그램) project.

## Reporting Vulnerabilities

If you discover a security vulnerability in this project, please report it to us at [rycbabd@gmail.com]. We appreciate your responsible disclosure and will make every effort to address the issue promptly.

When reporting a security vulnerability, please try to include as much information as possible, such as:

* A clear and concise description of the vulnerability.
* Steps to reproduce the vulnerability. Include specific input video files or actions if applicable.
* The affected version(s) of the "video_div" application.
* Any potential impact of the vulnerability (e.g., unexpected program behavior, file system manipulation if FFmpeg commands are crafted maliciously, etc.).
* Your name/handle (optional, but appreciated for acknowledging your contribution).

We are particularly interested in vulnerabilities related to:

* Improper handling of user-supplied file paths or FFmpeg parameters that could lead to command injection or arbitrary code execution (though the current implementation aims to prevent this by using fixed command structures).
* Issues that could cause denial of service (e.g., application crashes with specific inputs).
* Any other behavior that compromises user security or data integrity.

## Reporting Guidelines

To help us effectively address security vulnerabilities, please provide the following information in your report:

* A clear and concise description of the vulnerability.
* Steps to reproduce the vulnerability. Include specific input values or actions if applicable.
* The affected version(s) of the "video_div" application.
* Any potential impact of the vulnerability.
* Your name/handle (optional, but appreciated for acknowledging your contribution).

## Vulnerability Classification

We will assess the severity of reported vulnerabilities based on their potential impact. We encourage reporters to provide their own assessment of the severity, but we will make the final determination.

## Public Disclosure Policy

We will not publicly disclose vulnerabilities until a fix has been released and made available to users (e.g., via a new release on GitHub). We will credit responsible reporters in the release notes or commit messages (unless anonymity is requested).

## Scope

This security policy applies to the "video_div" application, including its Python source code and any distributed executable files. Please note that this policy does not cover vulnerabilities within FFmpeg itself; those should be reported to the FFmpeg project.

## Contact

For security-related inquiries regarding the "video_div" project, please contact us at [rycbabd@gmail.com].

---

# 보안 정책

이 문서는 "video_div" (Video Splitter / 동영상 분할 프로그램) 프로젝트의 보안 정책을 설명합니다.

## 취약점 보고

본 프로젝트에서 보안 취약점을 발견한 경우, [rycbabd@gmail.com]으로 보고해 주시기 바랍니다. 책임감 있는 제보에 감사드리며, 문제를 신속하게 해결하기 위해 최선을 다하겠습니다.

보안 취약점을 보고하실 때, 가능한 한 다음 정보를 포함해 주십시오:

* 취약점에 대한 명확하고 간결한 설명.
* 취약점을 재현하는 단계. 해당되는 경우 특정 입력 동영상 파일이나 동작을 포함합니다.
* "video_div" 애플리케이션의 영향을 받는 버전.
* 취약점의 잠재적 영향 (예: 예기치 않은 프로그램 동작, FFmpeg 명령어가 악의적으로 조작될 경우 파일 시스템 조작 등).
* 귀하의 이름/핸들 (선택 사항이지만, 기여에 대한 감사를 표하기 위해 권장합니다.)

특히 다음과 관련된 취약점에 관심이 있습니다:

* 명령어 주입 또는 임의 코드 실행으로 이어질 수 있는 사용자 제공 파일 경로 또는 FFmpeg 매개변수의 부적절한 처리 (현재 구현은 고정된 명령어 구조를 사용하여 이를 방지하는 것을 목표로 합니다).
* 서비스 거부(예: 특정 입력으로 인한 애플리케이션 충돌)를 유발할 수 있는 문제.
* 사용자 보안 또는 데이터 무결성을 손상시키는 기타 모든 동작.

## 보고 지침

보안 취약점을 효과적으로 해결할 수 있도록, 보고 시 다음 정보를 제공해 주십시오.

* 취약점에 대한 명확하고 간결한 설명
* 취약점을 재현하는 단계. 해당되는 경우 특정 입력 값 또는 동작을 포함합니다.
* "video_div" 애플리케이션의 영향을 받는 버전
* 취약점의 잠재적 영향
* 귀하의 이름/핸들 (선택 사항이지만, 기여에 대한 감사를 표하기 위해 권장합니다.)

## 취약점 분류

보고된 취약점의 심각도는 잠재적 영향을 기준으로 평가합니다. 보고자는 심각도에 대한 자체 평가를 제공할 수 있지만, 최종 결정은 저희가 내립니다.

## 공개 정책

당사는 수정 사항이 릴리스되어 사용자에게 제공될 때까지(예: GitHub의 새 릴리스를 통해) 취약점을 공개적으로 공개하지 않습니다. 익명을 요청하지 않는 한, 릴리스 노트 또는 커밋 메시지에 책임감 있는 보고자를 표기할 것입니다.

## 적용 범위

이 보안 정책은 "video_div" 애플리케이션의 Python 소스 코드 및 배포된 모든 실행 파일에 적용됩니다. 이 정책은 FFmpeg 자체 내의 취약점에는 적용되지 않으며, 해당 취약점은 FFmpeg 프로젝트에 보고해야 합니다.

## 연락처

"video_div" 프로젝트 관련 보안 문의는 [rycbabd@gmail.com]으로 연락 주시기 바랍니다.
