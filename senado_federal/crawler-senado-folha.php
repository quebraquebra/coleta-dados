<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
set_time_limit(0);

function escape($value) {
    return trim(strtoupper(str_replace('\'', '\\\'', $value)));
}

function mountDecimal($value) {
    if (!is_numeric($value)) {
        return 0;
    }

    return abs((float)preg_replace('/^(-?\d*)(\d{2})$/', '$1.$2', $value));
}

chdir('./csv');
$arquivos = glob('{*.csv}', GLOB_BRACE);

foreach ($arquivos as $arquivo) {
    $file = fopen($arquivo, 'r');

    while (!feof($file)) {
        $registro = explode(',', fgets($file));

        $servidor = escape($registro[1]);
        $vinculo = escape($registro[2]);
        $situacao = escape($registro[3]);
        $anoAdmissao = (int)$registro[4];
        $cargo = escape($registro[5]);
        $padrao = escape($registro[6]);
        $especialidade = escape($registro[7]);
        $mes = (int)$registro[8];
        $ano = (int)$registro[9];

        $tipo = 'NORMAL';
        $remuneracaoBasica = mountDecimal($registro[10]);
        $vantagensPessoais = mountDecimal($registro[11]);
        $funcaoCargoComissao = mountDecimal($registro[12]);
        $gratificacaoNatalina = mountDecimal($registro[13]);
        $horasExtras = mountDecimal($registro[14]);
        $outrasRemuneracoesEventuais = mountDecimal($registro[15]);
        $adicionalPericulosidade = mountDecimal($registro[16]);
        $adicionalNoturno = mountDecimal($registro[17]);
        $abonoPermanencia = mountDecimal($registro[18]);
        $reversao = mountDecimal($registro[19]);
        $impostoRenda = mountDecimal($registro[20]);
        $psss = mountDecimal($registro[21]);
        $faltas = mountDecimal($registro[22]);
        $diarias = mountDecimal($registro[24]);
        $auxilioAlimentacao = mountDecimal($registro[26]);
        $outrasVantagensIndenizatorias = mountDecimal($registro[27]);
        $licencaPremio = mountDecimal($registro[28]);

        $sql = "INSERT INTO folha_senado (tipo, ano, mes, servidor, ano_admissao, "
            . "vinculo, cargo, padrao, especialidade, situacao, "
            . "remuneracao_basica, vantagens_pessoais, funcao_cargo_comissao, gratificacao_natalina, "
            . "horas_extras, outras_remuneracoes_eventuais, "
            . "adicional_periculosidade, adicional_noturno, "
            . "abono_permanencia, reversao_teto_constitucional, imposto_renda, "
            . "psss, faltas, diarias, auxilio_alimentacao, outras_vantagens_indenizatorias, licenca_premio"
            . ") VALUES ("
            . "'{$tipo}', '${ano}', {$mes}, '{$servidor}', '{$anoAdmissao}', "
            . "'{$vinculo}', '{$cargo}', '{$padrao}', '{$especialidade}', '{$situacao}', "
            . "{$remuneracaoBasica}, {$vantagensPessoais}, {$funcaoCargoComissao}, {$gratificacaoNatalina}, "
            . "{$horasExtras}, {$outrasRemuneracoesEventuais}, "
            . "{$adicionalPericulosidade}, {$adicionalNoturno}, "
            . "{$abonoPermanencia}, {$reversao}, {$impostoRenda}, "
            . "{$psss}, {$faltas}, {$diarias}, {$auxilioAlimentacao}, {$outrasRemuneracoesEventuais}, {$licencaPremio} "
            . "),\r\n";

        $tipo = 'SUPLEMENTAR';
        $remuneracaoBasica = mountDecimal($registro[29]);
        $vantagensPessoais = mountDecimal($registro[30]);
        $funcaoCargoComissao = mountDecimal($registro[31]);
        $gratificacaoNatalina = mountDecimal($registro[32]);
        $horasExtras = mountDecimal($registro[33]);
        $outrasRemuneracoesEventuais = mountDecimal($registro[34]);
        $adicionalPericulosidade = mountDecimal($registro[35]);
        $adicionalNoturno = mountDecimal($registro[36]);
        $abonoPermanencia = mountDecimal($registro[37]);
        $reversao = mountDecimal($registro[38]);
        $impostoRenda = mountDecimal($registro[39]);
        $psss = mountDecimal($registro[40]);
        $faltas = mountDecimal($registro[41]);
        $diarias = mountDecimal($registro[43]);
        $auxilioAlimentacao = mountDecimal($registro[45]);
        $outrasVantagensIndenizatorias = mountDecimal($registro[46]);
        $licencaPremio = mountDecimal($registro[47]);

        $sql .= "('{$tipo}', '${ano}', {$mes}, '{$servidor}', '{$anoAdmissao}', "
            . "'{$vinculo}', '{$cargo}', '{$padrao}', '{$especialidade}', '{$situacao}', "
            . "{$remuneracaoBasica}, {$vantagensPessoais}, {$funcaoCargoComissao}, {$gratificacaoNatalina}, "
            . "{$horasExtras}, {$outrasRemuneracoesEventuais}, "
            . "{$adicionalPericulosidade}, {$adicionalNoturno}, "
            . "{$abonoPermanencia}, {$reversao}, {$impostoRenda}, "
            . "{$psss}, {$faltas}, {$diarias}, {$auxilioAlimentacao}, {$outrasRemuneracoesEventuais}, {$licencaPremio}"
            . ");\r\n";

        $sqlFile = fopen("../sql/senado-folha-{$ano}-{$mes}.sql", 'a');
        fwrite($sqlFile, $sql);
        fclose($sqlFile);
    }

    fclose($file);
}
