from django.shortcuts import render, get_object_or_404
from .models import TblCidade, TblPlano, TblAcordos, TblItens, TblFidelidade


def planos_by_city(request, cdd_id):
    city = get_object_or_404(TblCidade, cdd_id=cdd_id)
    
    # Use select_related ou prefetch_related para otimizar consultas
    planos = TblPlano.objects.filter(tblabrangenciaplano__abrang_cdd=city)

    for plano in planos:
        # Evite consultas adicionais usando prefetch_related ou select_related
        # plano.itens_combo = TblItensCombo.objects.filter(icomb_plan=plano).select_related('icomb_item')
        plano.itens = TblItens.objects.filter(tblitenscombo__icomb_plan=plano)
        plano.acordos = TblAcordos.objects.filter(acor_plan=plano)
        plano.fidelidade_disponivel = TblFidelidade.objects.filter(
            tblacordos__acor_plan=plano
        )

        for acordo in plano.acordos:
            plan_valor = acordo.acor_plan.plan_valor
            fid_qtdemeses = acordo.acor_fid.fid_qtdemeses
            acor_valor = acordo.acor_valor
            
            acordo.economia = (plan_valor * fid_qtdemeses) - (acor_valor * fid_qtdemeses)

    return render(
        request, 'planos/planos_by_city.html', {'city': city, 'planos': planos}
    )
