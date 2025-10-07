# catalog.py — Catálogo de 14 tipos con plantilla específica por ticket

CONFIRMATION_FALLBACK = (
    "El número de reporte asignado para su falla es : {INC}\n\n"
    "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
    "la cual estará notificando la solución con el número de reporte asignado.\n"
    "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
    "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
    "Reporte Asignado a:\n"
    "Grupo/Torre de Solución {GROUP}"
)

CATALOG: dict[str, dict] = {
    # 1) Generar Pedido - Tienda no programada
    "tienda_no_programada": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1001 0430",
        "classificationid":"150024530",
        "summary":"Tienda no programada",
        "group":"HELP DESK",
        "required":["full_name","phone"],
        "template": (
            "El número de reporte asignado para Tienda no Programada es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue atendido con el numero de folio de atención {INC}\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    }, # 1) Generar Pedido - Alta de pedido por tienda
    "alta_pedido_tienda": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1001 0434",
        "classificationid":"150024534",
        "summary":"Alta de pedido por tienda",
        "group":"HELP DESK",
        "required":["full_name","phone"],
        "template": (
            "El número de reporte asignado para Alta de Pedido por Tienda es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },

    # 2) Sincronizar Pedido
    "sync_pedido": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1001 0454",
        "classificationid":"150026521",
        "summary":"(CHAT) SYNC de Pedido",
        "group":"HELP DESK",
        "required":["full_name","phone"],
        "template": (
            "El número de reporte asignado para la Sincronización de Pedido es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue atendido con el numero de folio de atención {INC}\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },

    # 3) Revisar su Pedido
    "conciliacion_pedido": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"SIX1601 0103",
        "classificationid":"150024912",
        "summary":"Conciliación de pedido",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Conciliación de Pedido es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "producto_pendiente": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"SIX1601 0103",
        "classificationid":"150024912",
        "summary":"Producto pendiente (conciliación)",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Producto Pendiente en Pedido es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "salida_envase_incorrecta": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"150024930",
        "classificationid":"SIX1601 0121",
        "summary":"Salida de envase incorrecta",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Salida de Envase Incorrecta es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "dudas_monto_pagar": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1001 0443",
        "classificationid":"150024543",
        "summary":"Dudas Monto a Pagar",
        "group":"HELP DESK",
        "required":["description"],
        "template": (
            "El número de reporte asignado para Dudas de Monto a Pagar es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },

    # 4) Revisar entrada del Pedido
    "no_orden_entrada": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"SIX1601 0123",
        "classificationid":"150024932",
        "summary":"No se generó la orden de entrada",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para No Generación de Orden de Entrada es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )

    },
    "dudas_mov_envase": {
        "sev":"SEV 3 (IN)",
        "classstructureid":"SIX1601 0137",
        "classificationid":"100020452",
        "summary":"Dudas Movimiento de Envase",
        "group":"Block Networks",
        "required":["mrq_pe","a_envase","b_envase","c_envase"],
        "template": (
            "El número de reporte asignado para Dudas de Movimiento de Envase es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "dudas_recepcion_oe": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1306 0317",
        "classificationid":"150024686",
        "summary":"Dudas Recepción/Orden de Entrada",
        "group":"HELP DESK",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Dudas de Recepción / Orden de Entrada es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },

    # 5) Dudas sobre su Pedido
    "dudas_envase_a_entregar": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1306 0317",
        "classificationid":"150024686",
        "summary":"Dudas Envase a Entregar",
        "group":"HELP DESK",
        "required":["description"],
        "template": (
            "El número de reporte asignado para Dudas de Envase a Entregar es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "dudas_ventas_relacionadas": {
        "sev":"SEV 5 (SR)",
        "classstructureid":"SIX1001 0445",
        "classificationid":"150024545",
        "summary":"Dudas Ventas Relacionadas",
        "group":"HELP DESK",
        "required":["description"],
        "template": (
            "El número de reporte asignado para Dudas de Ventas Relacionadas es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },

    # Complementarios del flujo
    "ventas_incluidas_en_pedido": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"SIX1601 0103",
        "classificationid":"150024912",
        "summary":"Ventas incluidas (conciliación)",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Ventas Incluidas en Pedido es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
    "productos_a_recibir_en_pedido": {
        "sev":"SEV 2 (IN)",
        "classstructureid":"SIX1601 0123",
        "classificationid":"150024932",
        "summary":"Productos a recibir (entrada)",
        "group":"Block Networks",
        "required":["mrq_pe","description"],
        "template": (
            "El número de reporte asignado para Productos a Recibir en Pedido es : {INC}\n\n"
            "NOTA: Estimado usuario su reporte fue asignado a una área de solución encargada de analizar y resolver su incidencia,"
            "la cual estará notificando la solución con el número de reporte asignado.\n"
            "Si requiere dar SEGUIMIENTO al estatus de este Reporte,\n"
            "Seleccione la opción correspondiente en el MENÚ PRINCIPAL de este CHAT.\n\n"
            "Reporte Asignado a:\n"
            "Grupo/Torre de Solución {GROUP}"
        )
    },
}
