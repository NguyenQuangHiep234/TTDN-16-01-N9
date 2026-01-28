# -*- coding: utf-8 -*-
from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class CongViecRiskTrigger(models.Model):
    """Extend Cong Viec để tự động trigger AI risk analysis"""
    _inherit = 'cong_viec'
    
    @api.model
    def create(self, vals):
        """Tự động chạy AI khi tạo task mới"""
        task = super(CongViecRiskTrigger, self).create(vals)
        # Trigger AI analysis nếu task thuộc dự án
        if task.du_an_id:
            self._trigger_project_risk_analysis(task.du_an_id)
        return task
    
    def write(self, vals):
        """Tự động chạy AI khi cập nhật task"""
        result = super(CongViecRiskTrigger, self).write(vals)
        
        # Các field quan trọng trigger re-analysis
        important_fields = ['trang_thai', 'ti_le_hoan_thanh', 'ngay_ket_thuc', 'ngay_bat_dau']
        
        if any(field in vals for field in important_fields):
            for task in self:
                if task.du_an_id:
                    self._trigger_project_risk_analysis(task.du_an_id)
        
        return result
    
    def _trigger_project_risk_analysis(self, project):
        """Helper method để trigger AI analysis"""
        try:
            ai_engine = self.env['risk.ai.engine']
            ai_engine.analyze_project_risks(project.id)
            _logger.info(f"Auto AI analysis triggered for project {project.projects_id} by task change")
        except Exception as e:
            _logger.error(f"AI analysis failed: {str(e)}")


class BudgetsRiskTrigger(models.Model):
    """Extend Budgets để tự động trigger AI risk analysis"""
    _inherit = 'budgets'
    
    @api.model
    def create(self, vals):
        """Tự động chạy AI khi tạo budget mới"""
        budget = super(BudgetsRiskTrigger, self).create(vals)
        if budget.projects_id:
            self._trigger_project_risk_analysis(budget.projects_id)
        return budget
    
    def write(self, vals):
        """Tự động chạy AI khi cập nhật budget"""
        result = super(BudgetsRiskTrigger, self).write(vals)
        
        # Trigger khi budget-related fields thay đổi
        important_fields = ['budget_planned', 'budget_allocated', 'budget_spent']
        
        if any(field in vals for field in important_fields):
            for budget in self:
                if budget.projects_id:
                    self._trigger_project_risk_analysis(budget.projects_id)
        
        return result
    
    def _trigger_project_risk_analysis(self, project):
        """Helper method để trigger AI analysis"""
        try:
            ai_engine = self.env['risk.ai.engine']
            ai_engine.analyze_project_risks(project.id)
            _logger.info(f"Auto AI analysis triggered for project {project.projects_id} by budget change")
        except Exception as e:
            _logger.error(f"AI analysis failed: {str(e)}")


class ExpensesRiskTrigger(models.Model):
    """Extend Expenses để tự động trigger AI risk analysis"""
    _inherit = 'expenses'
    
    @api.model
    def create(self, vals):
        """Tự động chạy AI khi tạo expense mới"""
        expense = super(ExpensesRiskTrigger, self).create(vals)
        if expense.projects_id:
            self._trigger_project_risk_analysis(expense.projects_id)
        return expense
    
    def write(self, vals):
        """Tự động chạy AI khi cập nhật expense"""
        result = super(ExpensesRiskTrigger, self).write(vals)
        
        # Trigger khi expense amount thay đổi
        if 'expense_amount' in vals:
            for expense in self:
                if expense.projects_id:
                    self._trigger_project_risk_analysis(expense.projects_id)
        
        return result
    
    def _trigger_project_risk_analysis(self, project):
        """Helper method để trigger AI analysis"""
        try:
            ai_engine = self.env['risk.ai.engine']
            ai_engine.analyze_project_risks(project.id)
            _logger.info(f"Auto AI analysis triggered for project {project.projects_id} by expense change")
        except Exception as e:
            _logger.error(f"AI analysis failed: {str(e)}")
