import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3110.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT27/CH03673._CH', 'ED6_DT27/CH03673P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '希德中校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x152
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_171',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_18F)

    Jump('loc_18D')

    def _loc_171(): pass

    label('loc_171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_18D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_03_40E)

    def _loc_18D(): pass

    label('loc_18D')

    Return()

# id: 0x0001 offset: 0x18E
@scena.Code('func_01_18E')
def func_01_18E():
    Return()

# id: 0x0002 offset: 0x18F
@scena.Code('func_02_18F')
def func_02_18F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetPos(0x0008, 20700, 250, 262750, 180)
    ChrSetPos(0x0009, 21260, 0, 260470, 0)
    ChrSetPos(0x000A, 19790, 0, 260399, 45)
    CameraMove(21850, 0, 262980, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3190, 0)
    OP_6C(45000, 0)
    OP_6E(247, 0)
    FadeIn(2000, 0)
    PlaySE(133, 0x00, 0x64)

    @scena.Lambda('lambda_0242')
    def lambda_0242():
        OP_7C(50, 0, 1000, 3000)
        Yield()

        Jump('lambda_0242')

    DispatchAsync2(0x0101, 0x0003, lambda_0242)

    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0620230726V#702F#6P准将，这……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160230727V#1128F#5P嗯，我猜得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230728V看来，因慎重起见而中止了起降场的作业，\n',
            '这么做是对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600230729V#163F#4P唔唔，想不到会和你\n',
            '说的一样发生地震……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600230730V#160F卡西乌斯……\n',
            '你用了什么魔法？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160230731V#1120F#5P哪有……\n',
            '我只是站在对方的立场上想了一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160230732V#1125F想想在进行了三次『演习』之后……\n',
            '下一个目标放在哪里比较有效呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T3119._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x40E
@scena.Code('func_03_40E')
def func_03_40E():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(21350, 0, 262510, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetPos(0x0008, 20620, 300, 262810, 180)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000B, 20620, 0, 260040, 0)
    ChrClearFlags(0x000B, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#2440341416V──到此为止\n',
            '来自各方面的报告都已结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440341417V包括『埃尔赛尤』上的游击士在内\n',
            '大致上都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160341418V#1120F#5P呼……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440341419V不过就算是『结社』，\n',
            '说到底也只是个犯罪集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440341420V看来无法成为王国军的敌人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160341421V#1125F#5P别大意。\n',
            '那个『方舟』还在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160341422V#1122F警备艇继续对王国\n',
            '各地进行巡逻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160341423V另外，紧急指令\n',
            '要彻底传达到全军。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2440341424V明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)

    @scena.Lambda('lambda_0676')
    def lambda_0676():
        CameraMove(21810, 0, 258019, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0676)

    @scena.Lambda('lambda_068E')
    def lambda_068E():
        OP_67(0, 5000, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_068E)

    @scena.Lambda('lambda_06A6')
    def lambda_06A6():
        ChrWalkTo(0x00FE, 20830, 50, 252530, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_06A6)

    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(106, 0x00, 0x64)
    Sleep(500)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 0)

    @scena.Lambda('lambda_06DB')
    def lambda_06DB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_06DB)

    ChrWalkTo(0x000B, 20800, 0, 250500, 2500, 0x00)
    PlaySE(230, 0x00, 0x64)
    ChrClearFlags(0x000B, 0x0080)
    Sleep(500)

    Fade(500)
    CameraMove(21350, 0, 262510, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160341425V#1128F#5P紧急指令……\n',
            '在发生非常事件时的行动指令书吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160341426V#1125F希望这只是我杞人忧天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160341427V…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)

    @scena.Lambda('lambda_07FE')
    def lambda_07FE():
        CameraMove(20350, 0, 262510, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07FE)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 19790, 0, 263160, 270)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_084B')
    def lambda_084B():
        CameraMove(20640, 0, 265150, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_084B)

    ChrWalkTo(0x0008, 19940, 0, 264940, 2000, 0x00)
    Sleep(1000)

    PlaySE(131, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x00FF, 19800, 1180, 265350, 0, 0, 0, 250, 250, 250, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160341428V#1125F#6P──辛苦了。\n',
            '我是卡西乌斯·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160341429V#1120F不好意思，\n',
            '这么突然叫他来这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
