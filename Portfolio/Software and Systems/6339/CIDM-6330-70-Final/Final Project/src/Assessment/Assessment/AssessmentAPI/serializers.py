from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Customer, User, Project, ProposedProject, Assessment, AssessmentTemplate, AssessmentQuestion, Recommendation, RecommendationProposedProject, TechnologyInventory


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "name", "primary_location",
                  "alignment_engineer", "vcio")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email_address", "security_group")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "status", "project_manager", "cost",
                  "description", "customer", "completion_date")


class ProposedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposedProject
        fields = ("id", "name", "completion_date", "description", "customer")


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ("id", "date", "score", "percent_complete", "comments", "status",
                  "site_location", "assessment_template", "alignment_engineer", "customer")


class AssessmentTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentTemplate
        fields = ("id", "name", "assessment_type", "description")


class AssessmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentQuestion
        fields = ("id", "question", "answer", "support")


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ("id", "name", "completion_date", "description",
                  "status", "priority", "assessment", "customer")


class RecommendationProposedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationProposedProject
        fields = ("id", "recommendation", "proposed_project")


class TechnologyInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyInventory
        fields = ("id", "device_name", "site_location", "type", "make", "model", "serial_number", "operating_system",
                  "date_purchased", "date_warranty_expired", "age_years", "date_last_updated", "customer")
